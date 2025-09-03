import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms

# this class implements a model that, in the case of high suprise, acts on the pattern level of the world model
class Sys2Model(nn.Module):
    def __init__(self):
        super(Sys2Model, self).__init__()
        self.fc1 = nn.Linear(64*64, 128)