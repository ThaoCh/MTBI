'''
Notes:
	* N class Vnet for single channel 3d images
Args:
	* X of [BatchSize, Channel = 1, X-dim, Y-dim, Z-dim]
Out:
	* Y of [BatchSize, NumClasses, X-dim, Y-dim, Z-dim]
Source: 
	* This a modification of vnet.py implement forked from https://github.com/mattmacy/vnet.pytorch
Bug fix: 
	* Broadcasting bug in class InputTransition
	* ContBatchNorm3d substituded with native
'''

import torch
import torch.nn as nn
import torch.nn.functional as F

def passthrough(x, **kwargs):
	return x

def ELUCons(elu, nchan):
	'''
	Notes: 
		* using leaky activation function!
	Args:
		* elu: bool, using ELU activation or Not
		* nchan: int, number of channel for PReLU
	Return:
		* nn.Module
	'''
	if elu==True:
		return nn.ELU(inplace=True)
	else:
		return nn.PReLU(nchan)

class LUConv(nn.Module):
	'''
	Notes: 
		* 3d conv->bn->RELU, retain channel number
		* nchan: number of channel in and out
	'''
	def __init__(self, nchan, elu):
		super(LUConv, self).__init__()
		self.relu1 = ELUCons(elu, nchan)
		self.conv1 = nn.Conv3d(nchan, nchan, kernel_size=5, padding=2)
		self.bn1 = nn.BatchNorm3d(nchan)

	def forward(self, x):
		out = self.relu1(self.bn1(self.conv1(x)))
		return out

class ResLUConv(nn.Module):

	def __init__(nchan, elu):
		super(ResLUConv, self).__init__()
		self.conv1 = nn.Conv3d(nchan, nchan, kernel_size=5, padding=2)
		self.bn1 = nn.BatchNorm3d(nchan)
		self.relu1 = ELUCons(elu, nchan)

		self.conv2 = nn.Conv3d(nchan, nchan, kernel_size=5, padding=2)
		self.bn2 = nn.BatchNorm3d(nchan)
		self.relu2 = ELUCons(elu, nchan)

	def forward(self, x):

		out = self.relu1(self.bn1(self.conv1(x)))
		out = self.relu2(self.bn2(self.conv2(x)) + x)

		return out

def _make_rConv(nchan ,depth, elu):
	layers = []
	for _ in range(depth):
		layers.append(ResLUConv(nchan, elu))
	return nn.Sequential(*layers)

def _make_nConv(nchan, depth, elu):
	'''
	Notes:	
		* packaged conv3D layers
		* number = {2, 3}
	'''
	layers = []
	for _ in range(depth):
		layers.append(LUConv(nchan, elu))
	return nn.Sequential(*layers)

class InputTransition(nn.Module):
	'''
	Notes: 
		* X -> conv-> bn + X -> Relu
		* Bug fix in x16 = torch.cat
	'''
	def __init__(self, outChans, elu):
		super(InputTransition, self).__init__()
		self.conv1 = nn.Conv3d(12, outChans, kernel_size=5, padding=2)
		self.bn1 = nn.BatchNorm3d(outChans)
		self.relu1 = ELUCons(elu, outChans)

	def forward(self, x):
		# do we want a PRELU here as well?
		out = self.bn1(self.conv1(x))
		# (N, C, X, Y, Z) -> (N, 2C, X, Y, Z)
		xx = torch.cat((x, x), dim=1)
		out = self.relu1(torch.add(out, xx))

		return out

class DownTransition(nn.Module):
	'''
	Notes:
		* input -> conv/2-> bn -> relu -> X -> n*(conv3d->bn->relu) + X -> relu -> out
	'''
	def __init__(self, inChans, nConvs, elu, dropout=False):
		super(DownTransition, self).__init__()
		outChans = 2*inChans
		self.down_conv = nn.Conv3d(inChans, outChans, kernel_size=2, stride=2)
		self.bn1 = nn.BatchNorm3d(outChans)
		self.do1 = passthrough
		self.relu1 = ELUCons(elu, outChans)
		self.relu2 = ELUCons(elu, outChans)
		if dropout:
			self.do1 = nn.Dropout3d()
		self.ops = _make_nConv(outChans, nConvs, elu)

	def forward(self, x):
		down = self.relu1(self.bn1(self.down_conv(x)))
		out = self.do1(down)
		out = self.ops(out)
		out = self.relu2(torch.add(out, down))
		return out

class OutputTransition(nn.Module):
	def __init__(self, inChans, classnum, elu):

		'''
		Notes: 
			* converts to number of outputs
		Args:
			* inChans: input channels
			* classnum: number of classes
		Return:
			* None
		'''
		super(OutputTransition, self).__init__()
		class_num = 3
		self.conv1 = nn.Conv3d(inChans, 2, kernel_size=5, padding=2)
		self.bn1 = nn.BatchNorm3d(2)
		self.conv2 = nn.Conv3d(2, classnum, kernel_size=1)
		self.relu1 = ELUCons(elu, 2)

	def forward(self, x):
		# convolve 32 down to 2 channels
		out = self.relu1(self.bn1(self.conv1(x)))
		out = self.conv2(out)

		# out should have shape N, C, X, Y, Z at that time
		return out

class FCRB(nn.Module):
    def __init__(self, in_chan, out_chan):
        super(FCRB, self).__init__()
        self.affine = nn.Linear(in_chan, out_chan)
        self.bn = nn.BatchNorm1d(out_chan)
        self.relu = nn.ReLU(inplace=True)
        self.dp = nn.Dropout()

    def forward(self, x):
        out = self.dp(self.relu(self.bn(self.affine(x))))
        return out

class LNet(nn.Module):
	'''
	Half V Net
	'''
	def __init__(self, img_size, out_size=1, elu=True):
		'''
		Args:
			* slim: using few conv layers, else as original paper
			* elu: using elu / PReLU
		'''
		# 64*96*64 -> 4*6*4
		super(LNet, self).__init__()

		x, y, z = img_size

		self.in_tr = InputTransition(24, elu)
		self.down_tr32 = DownTransition(24, 2, elu, dropout=True) # /2
		self.down_tr64 = DownTransition(48, 3, elu, dropout=True) # /4
		self.down_tr128 = DownTransition(96, 3, elu, dropout=True) # /8
		self.down_tr256 = DownTransition(192, 4, elu, dropout=True) # /16
		self.gap = nn.AvgPool3d(kernel_size = (x//16,y//16,z//16)) # N, C, 1, 1, 1

		channel_num = 384

		self.fc1 = FCRB(channel_num, channel_num)
		self.fc2 = nn.Linear(channel_num, out_size)
		self.sigmoid = nn.Sigmoid()

	def forward(self, x):

		batch_size = x.size()[0] # get batch size

		out = self.in_tr(x)
		out = self.down_tr32(out)
		out = self.down_tr64(out)
		out = self.down_tr128(out)
		out = self.down_tr256(out)
		out = self.gap(out)
		out = out.view(batch_size, -1)

		out = self.fc1(out)
		out = self.fc2(out)
		out = self.sigmoid(out)

		return out
