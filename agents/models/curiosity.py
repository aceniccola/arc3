import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms

# this is the curiosity model that drives exploration. Any uncertanty in the world model would appear salient here.
class CuriosityModel(nn.Module):
    def __init__(self):
        super(CuriosityModel, self).__init__()
        self.fc1 = nn.Linear(64*64, 128)