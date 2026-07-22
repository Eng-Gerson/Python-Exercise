'''
We now build a very small neural network for regression.

The model has:

8 input neurons, one for each feature in the dataset
1 hidden layer with 5 neurons
ReLU activation after the hidden layer
1 output neuron, which predicts the house price
The architecture is:

8→5→1

Since this is a regression problem, the output layer has no activation function.

The model directly predicts a continuous numerical value.
'''

import torch
import torch.nn as nn

class HousePriceNN(nn.Module):
    def __init__(self):
        super().__init__()

        self.hidden = nn.Linear(8, 5)
        self.relu = nn.ReLU()
        self.output = nn.Linear(5, 1)

    def forward(self, x):
        x = self.hidden(x)
        x = self.relu(x)
        x = self.output(x)
        return x
