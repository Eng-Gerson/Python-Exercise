# Mini-competition: find the best model

You will now work independently on a regression task using the **Diabetes dataset**.

Your goal is to build the best neural network model you can.

The score is the **test loss**: the lower the score, the better the model.

---

### Data provided

You are given three dataloaders:

- `train_loader`
- `validation_loader`
- `test_loader`

Each dataloader contains input features and target values.

---

### Rules

You may use the **training set** to train the model parameters.

You may use the **validation set** to make modelling decisions, such as:

- number of hidden layers
- number of neurons per layer
- activation function
- learning rate
- batch size
- number of epochs
- optimizer
- regularization strategies

You must not use the **test set** while developing or tuning the model.

The test set must be used only once, at the end, after you have selected your final model.

---

### Correct workflow

1. Define a model architecture.
2. Train the model using only `train_loader`.
3. Evaluate it on `validation_loader`.
4. Modify the architecture or hyperparameters based on the validation loss.
5. Repeat until you choose your final model.
6. Evaluate the final model once on `test_loader`.

---

### Important

Do not choose the model based on the test loss.

If you use the test set repeatedly to improve your model, you are leaking information from the test set into the model development process.

This is called **data leakage**.

---

### Objective

Find the model with the lowest possible final test loss.

But remember:

> The competition is valid only if all model choices are made using the validation set, not the test set.