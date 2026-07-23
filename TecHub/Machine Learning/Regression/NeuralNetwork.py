import torch.nn as nn
class DiabetesNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.hidden = nn.Linear(10,32)
        self.relu = nn.Sigmoid()
        self.hidden2 = nn.Linear(32,32)
        self.leakyrelu = nn.LeakyReLU()
        self.output = nn.Linear(32,1)

    def forward(self,x):
        x = self.hidden(x)
        x = self.relu(x)
        x = self.hidden2(x)
        x = self.leakyrelu(x)
        x = self.output(x)
        return x

