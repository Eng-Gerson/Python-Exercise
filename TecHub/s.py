from sklearn.datasets import make_regression #Synthetic
from sklearn.datasets import make_classification
from sklearn.datasets import fetch_california_housing
from sklearn import datasets #Local

my_path = "./Test_data"
housing = fetch_california_housing(data_home=my_path, download_if_missing=False)

# Load the Iris dataset
iris = datasets.load_iris()

X = iris.data  # Features
y = iris.target # Target labels
print(f"Features shape: {X.shape}, Target shape: {y.shape}")

X_local, y_local = make_classification(
    n_samples=1000,
    n_features=5,
    n_classes=2,
    random_state=42
)
x_local, Y_local = make_regression(
    n_features= 4,
    n_samples= 10000,
    n_targets=1,
    n_informative=2,
    random_state=42
)
print(f"Synthetic features:{X_local.shape}")
print(f"Synthetic features:{x_local.shape}")
print("Done!")