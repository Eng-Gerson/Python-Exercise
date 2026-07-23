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

class DigitClassifierNN(nn.Module):
    def __init__(self):
        super().__init__()

        # Input: 28 x 28 image = 784 pixels
        self.hidden1 = nn.Linear(784, 10)
        self.relu1 = nn.ReLU()

        # Output: 10 neurons, one for each digit
        self.output = nn.Linear(10, 10)

        # Convert the 10 scores into probabilities
        self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        # x has shape: (batch_size, 1, 28, 28)

        # Flatten the image into a vector
        x = x.view(x.size(0), -1)

        # Neural network
        x = self.hidden1(x)
        x = self.relu1(x)
        x = self.output(x)
        x = self.softmax(x)

        return x