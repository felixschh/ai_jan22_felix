import torch
import torch.nn.functional as F
from torch import nn
# from torchsummary import summary

# YOUR CODE HERE
class Network(nn.Module):
    
    # Defining the layers
    def __init__(self):
        super(Network, self).__init__()
        self.fc1 = nn.Linear(8, 16)
        self.fc2 = nn.Linear(16, 8)
        self.fc3 = nn.Linear(8, 1)
        
    # Forward pass through
    def forward(self, x):
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        x = F.relu(x)
        x = self.fc3(x)
        return x

model = Network()
model

        