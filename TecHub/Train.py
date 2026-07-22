from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = {
    "code":[1,2,3,4,5,6,7,8,9,10,11],
    "age":[19, 20, 17, 17, 19, 21, 20, 18, 18, 17, 21],
    "mark": sorted([8, 1, 4, 6, 9, 2, 10, 3, 6, 5, 3])
}
Class = pd.DataFrame(data)
print(Class)
plt.scatter(Class["code"],Class["mark"])
plt.xlabel("Estudante")
plt.ylabel("Notas")
plt.title("Notas da classe")
plt.show()

X = Class.drop(columns=["mark"])
y = Class["mark"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.5,
    random_state= 5
)
print("X_train shape: ", X_train.shape)
print("y_train shape: ", y_train.shape)
print("X_test shape: ",X_test.shape)
print("y_test shape: ", y_test.shape)

model = DecisionTreeRegressor(
    max_depth=10,
    random_state= 5,
    min_samples_split= 2
)

model.fit(X_train, y_train)

y_pred_tree = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred_tree)
mse = mean_squared_error(y_test, y_pred_tree)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred_tree)

print("Max Depth = 5")
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)

plt.scatter(y_test, y_pred_tree)
plt.xlabel("True values")
plt.ylabel("Predictions")
plt.title("Max Depth = 5")
plt.show()