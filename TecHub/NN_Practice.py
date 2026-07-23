# My Neural Network in Practice
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from torch.utils.data import TensorDataset, DataLoader
from sklearn.preprocessing import StandardScaler
import torch
import torch.nn as nn
from NeuralNetwork import DiabetesNN
import matplotlib.pyplot as plt
# Reproducibility
seed = 42
torch.manual_seed(seed)
# Load dataset
data = load_diabetes(as_frame=True)

X = data.data
y = data.target

# First split: train+validation vs test
X_train_val, X_test, y_train_val, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=seed
)

# Second split: train vs validation
X_train, X_val, y_train, y_val = train_test_split(
    X_train_val,
    y_train_val,
    test_size=0.25,
    random_state=seed
)

# Final proportions:
# train = 60%
# validation = 20%
# test = 20%

# Scale features
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)
X_test_scaled = scaler.transform(X_test)

# Convert to PyTorch tensors
X_train_tensor = torch.tensor(X_train_scaled, dtype=torch.float32)
X_val_tensor = torch.tensor(X_val_scaled, dtype=torch.float32)
X_test_tensor = torch.tensor(X_test_scaled, dtype=torch.float32)

y_train_tensor = torch.tensor(y_train.values, dtype=torch.float32).view(-1, 1)
y_val_tensor = torch.tensor(y_val.values, dtype=torch.float32).view(-1, 1)
y_test_tensor = torch.tensor(y_test.values, dtype=torch.float32).view(-1, 1)

# Create datasets
train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
validation_dataset = TensorDataset(X_val_tensor, y_val_tensor)
test_dataset = TensorDataset(X_test_tensor, y_test_tensor)

# Create dataloaders
batch_size = 32

train_loader = DataLoader(
    train_dataset,
    batch_size=batch_size,
    shuffle=True
)

validation_loader = DataLoader(
    validation_dataset,
    batch_size=batch_size,
    shuffle=False
)
test_loader = DataLoader(
    test_dataset,
    batch_size=batch_size,
    shuffle=False
)

def evaluate_loss(modelo, data_loader, loss_fun):
    modelo.eval()

    total_Loss = 0.0
    total_Samples = 0

    with torch.no_grad():
        for X_Batch, y_Batch in data_loader:
            y_predict = modelo(X_Batch)
            Loss = loss_fun(y_predict, y_Batch)

            batch_size1 = X_Batch.shape[0]
            total_Loss += Loss.item() * batch_size1
            total_Samples += batch_size1

    average_loss = total_Loss / total_Samples

    return average_loss

n_epochs = 100
model = DiabetesNN()
loss_fn = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
train_loss, validation_loss = [], []

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

    train_loss.append(evaluate_loss(model, train_loader, loss_fn))
    validation_loss.append(evaluate_loss(model, validation_loader, loss_fn))

    epoch_loss = total_loss / total_samples
    print(f"Epoch {epoch}, training loss = {epoch_loss:.4f}")

plt.plot(train_loss, label="Train Loss")
plt.plot(validation_loss, label="Validation Loss")
plt.title("Loss")
plt.show()

print("Test Loss: ",evaluate_loss(model, test_loader, loss_fn))
# Validation: 2424 Test: 2719 with lr = 0.01, 10 -> 32 -> 32 -> 1 with ReLU and LeakyReLU
# Validation: 528 Test: 2765 with lr = 0.01, 10 -> 64 -> 32 -> 1 with LeakyReLU
# Validation: 537 Test: 2621 with lr = 0.01, 10 -> 64 -> 64 -> 1 with Sigmoid and ReLU
# Validation: Test: 2454 with lr = 0.01, 10 -> 32 -> 32 -> 1 with Sigmoid and LeakyReLU
