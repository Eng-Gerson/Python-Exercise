import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from torch.utils.data import TensorDataset, DataLoader
import torch
from Classifier import CancerClassifierNN


# Reproducibility
seed = 42
batch_size = 32

np.random.seed(seed)
torch.manual_seed(seed)


# Load dataset
data = load_breast_cancer(as_frame=True)

X = data.data
y = data.target

# Optional: invert labels so that
# 0 = benign
# 1 = malignant
y = 1 - y


# Split: train+validation vs test
X_train_val, X_test, y_train_val, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=seed,
    stratify=y
)

# Split: train vs validation
X_train, X_val, y_train, y_val = train_test_split(
    X_train_val,
    y_train_val,
    test_size=0.25,
    random_state=seed,
    stratify=y_train_val
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

# Convert to tensors
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

# Create loaders
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

# Create model
model = CancerClassifierNN()

# Loss and optimizer
loss_fn = nn.BCELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Training settings
n_epochs = 100

train_losses = []
validation_losses = []

for epoch in range(n_epochs):

    # ---- Training phase ----
    model.train()

    total_train_loss = 0.0
    total_train_samples = 0

    for X_batch, y_batch in train_loader:

        # Forward pass
        y_pred = model(X_batch)

        # Compute loss
        loss = loss_fn(y_pred, y_batch)

        # Backpropagation
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        # Accumulate loss
        batch_size = X_batch.shape[0]
        total_train_loss += loss.item() * batch_size
        total_train_samples += batch_size

    train_loss = total_train_loss / total_train_samples
    train_losses.append(train_loss)


    # ---- Validation phase ----
    model.eval()

    total_val_loss = 0.0
    total_val_samples = 0

    with torch.no_grad():
        for X_batch, y_batch in validation_loader:

            y_pred = model(X_batch)
            loss = loss_fn(y_pred, y_batch)

            batch_size = X_batch.shape[0]
            total_val_loss += loss.item() * batch_size
            total_val_samples += batch_size

    val_loss = total_val_loss / total_val_samples
    validation_losses.append(val_loss)


    # Print progress
    if epoch % 10 == 0:
        print(
            f"Epoch {epoch:3d} | "
            f"train loss = {train_loss:.4f} | "
            f"validation loss = {val_loss:.4f}"
        )