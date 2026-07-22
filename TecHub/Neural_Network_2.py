'''
## Can't believe it is not better!

We have made the neural network deeper.

Intuitively, we might expect:

> more layers = better model

However, this is not always true.

A deeper network has more parameters and can represent more complex functions, but it can also become harder to train.

One possible issue is that gradients may become very small while they are propagated backward through the network.

When this happens, the first layers receive very weak updates and learn very slowly.

This is known as the **vanishing gradient problem**.

---

### Small experiment

Now modify the model and test what happens.

1. Replace the ReLU activation:

```python
nn.ReLU()
```
with a sigmoid activation:
```python
nn.Sigmoid()
```

2. Add more hidden layers (try 1, 5, 10, 15, 20)
3. Train the model again.
4. Compare:

* training loss
* test loss
* training curve
'''
#Neural Network with custom number of layers
import torch
import torch.nn as nn
class HousePriceNN(nn.Module):
    def __init__(self, n_hidden_layers):
        super().__init__()

        self.hidden_layers = nn.ModuleList()

        # First hidden layer: 8 input features -> 64 neurons
        self.hidden_layers.append(nn.Linear(8, 32))

        # Remaining hidden layers: 32 -> 32
        for _ in range(n_hidden_layers - 1):
            self.hidden_layers.append(nn.Linear(32, 32))

        self.sigmoid = nn.Sigmoid()
        self.output = nn.Linear(32, 1)

    def forward(self, x):
        for layer in self.hidden_layers:
            x = layer(x)
            x = self.sigmoid(x)

        x = self.output(x)
        return x

##How a model can be created with a specific number of layers
## model = HousePriceNN(2)