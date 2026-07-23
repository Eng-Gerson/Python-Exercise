import torch.nn as nn
class CancerClassifierNN(nn.Module):
    def __init__(self):
        super().__init__()

        # Input size: 30 features
        # TODO: define the neural network layers here
        self.hidden = nn.Linear(30, 50)
        self.activation = nn.ReLU()
        self.output = nn.Linear(50, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.hidden(x)
        x = self.activation(x)
        x = self.output(x)
        x = self.sigmoid(x)
        return x