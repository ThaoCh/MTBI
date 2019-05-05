import datetime

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.optim.lr_scheduler import ReduceLROnPlateau
from scipy.ndimage import affine_transform, zoom

from niiutility import *
from scipy.ndimage import affine_transform, zoom, gaussian_filter

def accuracy(output, target):
    '''
    Acc helper translated from Dr.kyamagu:
    https://gist.github.com/kyamagu/73ab34cbe12f3db807a314019062ad43
    taking input (N, 2)
    '''
    
    output = (output.cpu()).detach().numpy()
    target = (target.cpu()).detach().numpy()
    
    out_one = np.argmax(output, axis=1)
    
    pred = (out_one >= 0.5).astype(np.float32)
    truth = (target >= 0.5).astype(np.float32)

    correct = (pred == truth).astype(np.float32)

    acc = np.sum(correct) / correct.shape[0]
    return acc

def weights_init(m):
    classname = m.__class__.__name__
    
    if classname.find('Conv3d') != -1:
        nn.init.kaiming_normal_(m.weight)
        m.bias.data.zero_()

    if type(m) == nn.Linear:
        torch.nn.init.xavier_uniform_(m.weight)

def shape_test(model, device, dtype, lossFun, shape):
    
    sx, sy, sz = shape

    x = torch.randn((24, 3, sx, sy, sz), dtype=dtype, requires_grad=True)
    y = torch.ones((24, 3, sx, sy, sz), dtype=dtype, requires_grad=True)

    # model = model.to(device=device)
    # scores = model(x)
    # print(scores.size())
    loss = lossFun(x, y, cirrculum=2)

def loadckp (model, optimizer, scheduler, filename, device):
    model = model.to(device=device)
    if os.path.isfile(filename):
        print("loading checkpoint '{}'".format(filename))
        checkpoint = torch.load(filename)
        start_epoch = checkpoint['epoch']
        model.load_state_dict(checkpoint['state_dict'])
        optimizer.load_state_dict(checkpoint['optimizer'])
        scheduler.load_state_dict(checkpoint['scheduler'])
        print("loaded checkpoint '{}' (epoch {})"
                  .format(filename, checkpoint['epoch']))
    else:
        print("no checkpoint found at '{}'".format(filename))

    return model, optimizer, scheduler

def train(model, traindata, valdata, optimizer, scheduler, device, dtype, lossFun, epochs=1, streopch=0):
    """
    Train a model with an optimizer
    
    Inputs:
    - model: A PyTorch Module giving the model to train.
    - optimizer: An Optimizer object we will use to train the model
    - epochs: (Optional) A Python integer giving the number of epochs to train for
    
    Returns: Nothing, but prints model accuracies during training.
    """
    model = model.to(device=device)  # move the model parameters to CPU/GPU
    N = len(traindata)
    for e in range(epochs):
        epoch_loss = 0
        acc = 0
        for t, batch in enumerate(traindata):
            model.train()  # put model to training mode
            x = batch['image']
            y = batch['label'].view(-1)
            x = x.to(device=device, dtype=dtype)  # move to device, e.g. GPU
            y = y.to(device=device, dtype=torch.long)
            
            scores = model(x)
            
            loss = lossFun(scores, y)
            
            # avoid gradient
            epoch_loss += loss.item()
            acc += accuracy(scores, y) #this is not even a tensor...

            # Zero out all of the gradients for the variables which the optimizer
            # will update.
            optimizer.zero_grad()

            # This is the backwards pass: compute the gradient of the loss with
            # respect to each  parameter of the model.
            loss.backward()

            # Actually update the parameters of the model using the gradients
            # computed by the backwards pass.
            optimizer.step()
            
        print('Epoch {0} finished ! Training Loss: {1:.4f}, acc: {2:.4f}'.format(e + streopch, epoch_loss/N, acc/N))
        
        loss_val = check_accuracy(model, valdata, device, dtype, lossFun=lossFun)
        # scheduler.step(loss_val)
           
        # When validation loss < 0.1,upgrade cirrculum, reset scheduler
        if (e + streopch) % 50 == 0:
            model_save_path = 'checkpoint' + str(datetime.datetime.now())+'.pth'
            state = {'epoch': e + streopch + 1, 'state_dict': model.state_dict(),
                'optimizer': optimizer.state_dict(), 'scheduler': scheduler.state_dict()}
            torch.save(state, model_save_path)
            print('Checkpoint {} saved !'.format(e + streopch + 1))
        
def check_accuracy(model, dataloader, device, dtype, lossFun):
    model.eval()  # set model to evaluation mode
    with torch.no_grad():
        loss = 0
        acc = 0
        N = len(dataloader)
        for t, batch in enumerate(dataloader):
            x = batch['image']
            y = batch['label'].view(-1)
            x = x.to(device=device, dtype=dtype)  # move to device, e.g. GPU
            y = y.to(device=device, dtype=torch.long)
            scores = model(x)
            
            loss += lossFun(scores, y)
            acc += accuracy(scores, y)

        print('     validation loss = {0:.4f}, accuracy = {1:.4f}'.format (loss/N, acc/N))
        return loss/N
