"""
## Why do we scale the input features?

Neural networks are sensitive to the scale of the input variables.

In this dataset, different features have very different numerical ranges.
For example, one variable may represent income, another one may represent the average number of rooms, and another one may represent geographical coordinates.

If we use these variables directly, features with larger numerical values may dominate the computation inside the network.

A neural network computes weighted sums such as:

$z = w_1x_1 + w_2x_2 + dots + w_nx_n + b$

If some input variables are much larger than others, their contribution to this sum can become disproportionately large.
This can make training slower, less stable, and harder for the optimizer.

Scaling transforms the features so that they have comparable ranges.

A common approach is standardization:

$x_{\text{scaled}} = \frac{x - mu}{sigma}$

where:

- $mu$ is the mean of the feature
- $sigma$ is the standard deviation of the feature

After standardization, each feature has approximately:

- mean equal to 0
- standard deviation equal to 1

This usually helps the neural network train more efficiently and more reliably.
**Important:** the scaler is fitted only on the training data.

We use:
This avoids leaking information from the test set into the training process.
"""
from sklearn.datasets import fetch_california_housing
from torch.utils.data import TensorDataset, DataLoader
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from Neural_Network import HousePriceNN
import torch
import pandas as pd
import torch.nn as nn
import matplotlib.pyplot as plt


# Load the dataset as a pandas DataFrame
housing = fetch_california_housing(as_frame=True)

# Full dataframe: features + target
df = housing.frame

# Rename target column to something more intuitive
df = df.rename(columns={"MedHouseVal": "price"})

# Show first rows
df.head()

plt.figure(figsize=(12, 5))

X = df.drop(columns=["price"])
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

X_train.boxplot(rot=45, showfliers=False)

plt.title("Box plots of training features before scaling")
plt.ylabel("Feature value")
plt.tight_layout()
plt.show()

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

X_train_scaled_df = pd.DataFrame(
    X_train_scaled,
    columns=X_train.columns,
    index=X_train.index
)
plt.figure(figsize=(12, 5))

X_train_scaled_df.boxplot(rot=45, showfliers=False)

plt.title("Box plots of training features after scaling")
plt.ylabel("Feature value")
plt.tight_layout()
plt.show()
#---------------------------------#
#        Neural Network           #
#---------------------------------#

#Our tensor
batch_size = 32

X_train_tensor = torch.tensor(X_train_scaled, dtype=torch.float32)
X_test_tensor = torch.tensor(X_test_scaled, dtype=torch.float32)

y_train_tensor = torch.tensor(y_train.values, dtype=torch.float32).view(-1, 1)
y_test_tensor = torch.tensor(y_test.values, dtype=torch.float32).view(-1, 1)


train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
test_dataset = TensorDataset(X_test_tensor, y_test_tensor)

train_loader = DataLoader(
    train_dataset,
    batch_size=batch_size,
    shuffle=True
)

test_loader = DataLoader(
    test_dataset,
    batch_size=batch_size,
    shuffle=False
)

'''
## Training with mini-batches

Instead of using the entire training set at once, we train the neural network using mini-batches.

At each step, the model sees only a small subset of the training data.

For each mini-batch, PyTorch performs the same sequence of operations:

1. Compute the predictions
2. Compute the loss
3. Compute the gradients
4. Update the model parameters

This process is repeated for all batches in the training set.

One complete pass over the full training set is called an **epoch**.
'''
n_epochs = 10
model = HousePriceNN()

loss_fn = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

for epoch in range(n_epochs):

    model.train()

    total_loss = 0.0
    total_samples = 0

    for X_batch, y_batch in train_loader:

        y_pred = model(X_batch)
        loss = loss_fn(y_pred, y_batch)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        batch_size = X_batch.shape[0]
        total_loss += loss.item() * batch_size
        total_samples += batch_size

    epoch_loss = total_loss / total_samples


    print(f"Epoch {epoch}, training loss = {epoch_loss:.4f}")
