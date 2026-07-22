from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset as a pandas DataFrame
housing = fetch_california_housing(as_frame=True)

# Full dataframe: features + target
df = housing.frame

# Rename target column to something more intuitive
df = df.rename(columns={"MedHouseVal": "price"})

# Show first rows
df.head()
df.columns()
df.describe()
df.isnull().sum()
#-----------------------------------------#
#Visualize the distribution of house prices
#'MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup',
# 'Latitude', 'Longitude',
plt.figure(figsize=(6, 4))
plt.hist(df["MedInc"],bins= 50)
plt.scatter(df['MedInc'], df['price'])

#Machine Learning Train_Test_Split

# Separate features and target
X = df.drop(columns=["price"]) #Features
y = df["price"] #Target

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,      # 20% test, 80% training
    random_state=27    # reproducible split
)

print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)
print("X_test shape:", X_test.shape)
print("y_test shape:", y_test.shape)


# Define a single regression tree with maximum depth 3
tree_model = DecisionTreeRegressor(
    max_depth=36,
    random_state=27,
    min_samples_split=2,
)

# Train the model
tree_model.fit(X_train, y_train)


# Predict on the test set
y_pred_tree = tree_model.predict(X_test)

# Evaluate
mae = mean_absolute_error(y_test, y_pred_tree) # sum of all pred |p - r|
mse = mean_squared_error(y_test, y_pred_tree) # sum of all pred (p-r)^2
rmse = np.sqrt(mse)# ( sum of all pred(p-r)^2 )^0.5
r2 = r2_score(y_test, y_pred_tree)

print("Decision Tree Regressor, max_depth=3")
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)

plt.scatter(y_test, y_pred_tree)
plt.xlabel("True values")
plt.ylabel("Predictions")
plt.title("Decision Tree Regressor, max_depth=3")

def Task1():
    X = df.drop(columns=["price"])  # Features
    y = df["price"]  # Target

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,  # 20% test, 80% training
        random_state=27  # reproducible split
    )
    # Values of max_depth to test
    max_depth_values = [3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 20, 35, 40, 50]

    # Store results
    results = []

    for depth in max_depth_values:

        # Define the model
        model = DecisionTreeRegressor(
         max_depth=depth,
         random_state=42
        )

        # Train the model on the training set
        model.fit(X_train, y_train)

        # Predict on the test set
        y_pred = model.predict(X_test)

        # Compute metrics
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_pred)

        # Save results
        results.append({
         "max_depth": depth,
         "MAE": mae,
         "MSE": mse,
         "RMSE": rmse,
        })

    # Convert to dataframe
    results_df = pd.DataFrame(results)

    results_df

    plt.figure(figsize=(6, 4))
    plt.plot(results_df["max_depth"], results_df["MAE"], marker="o")
    plt.xlabel("Number of trees")
    plt.ylabel("Mean Absolute Error")
    plt.title("Effect of the Number of Trees on Test Error")
    plt.show()

    # Define a single regression tree with maximum depth 3
    tree_model = DecisionTreeRegressor(
     max_depth=9,
     random_state=42,
     min_samples_split=2,
    )   

    # Train the model
    tree_model.fit(X_train, y_train)
    
    # Predict on the test set
    y_pred_tree = tree_model.predict(X_test)

    # Evaluate
    mae = mean_absolute_error(y_test, y_pred_tree)
    mse = mean_squared_error(y_test, y_pred_tree)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred_tree)

    print("Decision Tree Regressor, max_depth=3")
    print("MAE:", mae)
    print("MSE:", mse)
    print("RMSE:", rmse)

    plt.scatter(y_test, y_pred_tree)
    plt.xlabel("True values")
    plt.ylabel("Predictions")
    plt.title("Decision Tree Regressor, max_depth=3")

    # Separate features and target
    X = df.drop(columns=["price"])
    y = df["price"]

    # Split into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(
     X,
     y,
     test_size=0.2,      # 50% test, 50% training
     random_state=42     # reproducible split
    )

    print("X_train shape:", X_train.shape)
    print("y_train shape:", y_train.shape)
    print("X_test shape:", X_test.shape)
    print("y_test shape:", y_test.shape)
    max_depth_values = [3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 20, 35, 40, 50]

    # Store results
    results = []

    for depth in max_depth_values:
     # Define the model
     model = DecisionTreeRegressor(
         max_depth=depth,
         random_state=42
     )

     # Train the model on the training set
     model.fit(X_train, y_train)

     # Predict on the test set
     y_pred = model.predict(X_test)

     # Compute metrics
     mae = mean_absolute_error(y_test, y_pred)
     mse = mean_squared_error(y_test, y_pred)
     rmse = np.sqrt(mse)
     r2 = r2_score(y_test, y_pred)

     # Save results
     results.append({
         "max_depth": depth,
         "MAE": mae,
         "MSE": mse,
         "RMSE": rmse,
     })

    # Convert to dataframe
    results_df80 = pd.DataFrame(results)

    results_df80

    plt.figure(figsize=(6, 4))
    plt.plot(results_df["max_depth"], results_df["MAE"], marker="o", label="50%")
    plt.plot(results_df80["max_depth"], results_df80["MAE"], marker="o", label="80%")
    plt.xlabel("Number of trees")
    plt.ylabel("Mean Absolute Error")
    plt.title("Effect of the Number of Training Points")
    plt.legend()
