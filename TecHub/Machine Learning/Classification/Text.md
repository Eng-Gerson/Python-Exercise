## Exercise: build a neural network for binary classification

Create a neural network to predict whether a sample is **benign** or **malignant**.

The input size is fixed by the dataset:


$30$


because each patient is described by 30 numerical features.

Your task is to complete the neural network architecture.

Requirements:

- the model must take 30 input features;
- the model must output a single value;
- the final output must be passed through a `Sigmoid`;
- the output should be interpreted as the predicted probability of the positive class;
- use `nn.BCELoss()` as the loss function.

## Didactic implementation

In this section, we implement the multi-class classifier in a deliberately explicit way.

The neural network will end with a `Softmax` layer, so its output will be a vector of probabilities:

$$
[p_0, p_1, \dots, p_9]
$$

where each value represents the predicted probability of one class.

We will also implement the cross-entropy loss manually, in order to see what the loss function is actually computing.

This is useful for didactic purposes.

However, this is **not the standard way to train multi-class classifiers in PyTorch**.

Later, we will see the usual PyTorch implementation, where the model outputs raw scores, called **logits**, and the loss is computed using:

```python
nn.CrossEntropyLoss()
```

## From images to vectors

MNIST images are grayscale images of handwritten digits.

Each image has size:

$$
28 \times 28
$$

This means that each image contains:

$$
28 \cdot 28 = 784
$$

pixels.

A fully connected neural network cannot directly process the image as a 2D grid.

So we first **flatten** the image into a vector:

$$
28 \times 28 \longrightarrow 784
$$

The image becomes a vector of 784 input values, one for each pixel.

---

## Network idea

We can now build a neural network with:

$$
784 \rightarrow \dots \rightarrow 10 \rightarrow \mathrm{Softmax}
$$

where:

- 784 is the number of input pixels;
- the intermediate layers learn useful combinations of pixels;
- 10 is the number of output classes;
- Softmax converts the 10 output scores into probabilities.

The final output is a probability distribution over the ten possible digits:

$$
0, 1, 2, 3, 4, 5, 6, 7, 8, 9
$$

During training, the network learns to assign high probability to the correct digit.

## Mini-challenge: improve the digit classifier

You are now given a neural network for MNIST digit classification.

The input is a flattened image:

$$ 28 \times 28 = 784 $$

The output contains 10 neurons, one for each digit:


$$ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 $$

Your task is to modify the topology of the network and try to improve its performance.

---

### What you can modify

You may change:

- the number of hidden layers;
- the number of neurons in each hidden layer;
- the activation functions;
- the learning rate;
- the batch size.

You must keep:

- 784 input values;
- 10 output neurons;
- Softmax as the final layer;
- the manually implemented cross-entropy loss.

---

### Validation set

Use the **training set** to update the network weights.

Use the **validation set** to compare different models.

For each model, report:

- training loss;
- validation loss;
- validation accuracy.

Choose the final model using only the validation set.

---

### Test set

The test set must be used only once.

After you have selected your final model, evaluate it on the test set and report the final test accuracy.

Do not use the test set to choose the model.

---

### Constraint

You can train each model for at most:

$$10$$

epochs.

---

### Goal

Find the network topology that gives the best validation accuracy.

Then evaluate the selected model once on the test set.

