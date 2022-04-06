#import the needed libraries

import data_handler as dh           # yes, you can import your code. Cool!
import torch
import torch.optim as optim
import torch.nn as nn

import matplotlib.pyplot as plt
import numpy as np

from model import Network

x_train, x_test, y_train, y_test = dh.load_data('Chapter 03/03. MLP Regression/data/turkish_stocks.csv')

model = Network()

lr = 1e-1
n_epochs = 100

optimizer = torch.optim.SGD(model.parameters(), lr=0.2)
loss_func = torch.nn.MSELoss()

for epoch in range(n_epochs):
    model.train()
    optimizer.zero_grad()

    y_hat = model(x_train)
    
    loss = loss_func(y_train, y_hat)
    loss.backward()    
    optimizer.step()
    losses = loss.item()

    
train_loader = dh.to_batches(x_train, x_test, y_train, y_test, 20)

losses = []
val_losses = []

for epoch in range(n_epochs):
    for x_batch, y_batch in train_loader:
        x_batch = x_batch
        y_batch = y_batch

        loss = losses(x_batch, y_batch)
        losses.append(loss)
        
    with torch.no_grad():
        for x_val, y_val in val_loader:
            x_val = x_val
            y_val = y_val
            
            model.eval()

            yhat = model(x_val)
            val_loss = loss_func(y_val, yhat)
            val_losses.append(val_loss.item())

print(model.state_dict())


# Remember to validate your model: with torch.no_grad() ...... model.eval .........model.train
