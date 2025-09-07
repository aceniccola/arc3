import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms

# this is the policy network that makes decisions about what to do in the world
class PolicyModel(nn.Module):
    def __init__(self, embedding_size):
        super(PolicyModel, self).__init__()
        self.fc1 = nn.Linear(64*64, 128)
        self.activation1 = nn.ReLU()
        self.fc2 = nn.Linear(128, 10)
        self.activation2 = nn.Softmax(dim=1)

    def forward(self, x):
        x = self.fc1(x)
        x = self.activation1(x)
        x = self.fc2(x)
        x = self.activation2(x)
        print(x)
        return x
