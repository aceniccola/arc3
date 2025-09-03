import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms

# this is the higher order world model that looks at long term hypotheses about the world (does having a second order model have a significant impact on sample efficiency?)
# this is in conceptual space rather than reality space. Which one should be larger?
class SCI(nn.Module):
    def __init__(self):
        super(SCI, self).__init__()
        self.fc1 = nn.Linear(64*64, 128)