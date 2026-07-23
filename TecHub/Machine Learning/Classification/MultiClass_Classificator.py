from torchvision.datasets import MNIST
from torchvision import transforms
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
import torch
from Classifier import DigitClassifierNN

transform = transforms.ToTensor()

train_dataset = MNIST(
    root="data",
    train=True,
    download=True,
    transform=transform
)

test_dataset = MNIST(
    root="data",
    train=False,
    download=True,
    transform=transform
)

train_loader = DataLoader(
    train_dataset,
    batch_size=64,
    shuffle=True
)

test_loader = DataLoader(
    test_dataset,
    batch_size=64,
    shuffle=False
)

# Take the first 9 MNIST images
images = []
labels = []

for i in range(9):
    image, label = train_dataset[i]
    images.append(image)
    labels.append(label)

# Plot them in a 3 x 3 grid
fig, axes = plt.subplots(3, 3, figsize=(6, 6))

for i, ax in enumerate(axes.ravel()):
    ax.imshow(images[i].squeeze(), cmap="gray")
    ax.set_title(f"Label: {labels[i]}")
    ax.axis("off")

plt.tight_layout()
plt.show()

#definition of the loss function
def categorical_cross_entropy(probabilities, targets):
    eps = 1e-8

    # Avoid log(0), which is undefined
    probabilities = torch.clamp(probabilities, eps, 1.0)

    # Select the predicted probability assigned to the correct class
    correct_class_probabilities = probabilities[
        torch.arange(len(targets)), targets
    ]

    # Cross-entropy loss
    loss = -torch.log(correct_class_probabilities)

    # Average loss over the batch
    return loss.mean()

#training loop
# Create model
model = DigitClassifierNN()

# Manual loss function
loss_fn = categorical_cross_entropy

# Optimizer
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Training settings
n_epochs = 5

train_losses = []

for epoch in range(n_epochs):

    model.train()

    total_loss = 0.0
    total_samples = 0

    for X_batch, y_batch in train_loader:

        # y_batch must contain class indices: 0, 1, ..., 9
        y_batch = y_batch.long()

        # Forward pass
        probabilities = model(X_batch)

        # Manual cross-entropy loss
        loss = loss_fn(probabilities, y_batch)

        # Backpropagation
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        # Accumulate loss
        batch_size = X_batch.shape[0]
        total_loss += loss.item() * batch_size
        total_samples += batch_size

    epoch_loss = total_loss / total_samples
    train_losses.append(epoch_loss)

    print(f"Epoch {epoch + 1}/{n_epochs} - loss: {epoch_loss:.4f}")