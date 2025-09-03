import random
import time
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms

# this class increases the sample efficiency of the policy network by learning a model of the world
# this class takes in the array of sensory data and outputs a 'model' of the world. This is a high dimensional embedding of the world.
# in other settings, we can give it the abillity to learn the future step from a past steo by obveserving.
# However, in this situation, we can bias our model to assume that only their own actions can change the world. 
# therefore, the only uses come out of either undertanding the current world state or underanding the state of the world after their most perfered current action.
class WorldModel(nn.Module):
    def __init__(self):
        super(WorldModel, self).__init__()
        self.encoder = nn.Sequential(
            nn.Linear(64*64, 128),
            nn.ReLU(),
            nn.Linear(128, 64*64)
        )
        self.fc1 = nn.Linear(64*64, 128)
        self.fc2 = nn.Linear(128, 64*64)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x