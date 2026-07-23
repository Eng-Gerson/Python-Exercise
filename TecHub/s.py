from sklearn.datasets import make_regression #Synthetic
from sklearn.datasets import make_classification
from sklearn.datasets import fetch_california_housing
from sklearn.datasets import load_diabetes
from sklearn import datasets #Local

my_path = "./Test_data"
housing = fetch_california_housing(data_home=my_path, download_if_missing=False)
diabetes = load_diabetes
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

"""
Exemplo: treinar uma rede neural com PyTorch usando 3 conjuntos
de dados (treino / validação / teste), com early stopping baseado
na perda de validação.

Requisitos:
    pip install torch scikit-learn
"""

import copy
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report


# ------------------------------------------------------------------
# 1. Dados: dividir em treino (~70%), validação (~15%) e teste (~15%)
# ------------------------------------------------------------------
data = load_wine()
X, y = data.data, data.target

# Primeiro separa o teste — ele fica de fora e só é usado no final
X_temp, X_test, y_temp, y_test = train_test_split(
    X, y, test_size=0.15, random_state=42, stratify=y
)

# Depois separa treino e validação a partir do que sobrou
X_train, X_val, y_train, y_val = train_test_split(
    X_temp, y_temp, test_size=0.1765, random_state=42, stratify=y_temp
)  # 0.1765 * 0.85 ≈ 0.15 -> cada conjunto fica com ~70/15/15%

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)
X_test = scaler.transform(X_test)


def to_tensor(X, y):
    return torch.tensor(X, dtype=torch.float32), torch.tensor(y, dtype=torch.long)


X_train_t, y_train_t = to_tensor(X_train, y_train)
X_val_t, y_val_t = to_tensor(X_val, y_val)
X_test_t, y_test_t = to_tensor(X_test, y_test)

print(f"Treino: {len(X_train)} | Validação: {len(X_val)} | Teste: {len(X_test)}")


# ------------------------------------------------------------------
# 2. Modelo
# ------------------------------------------------------------------
class RedeNeural(nn.Module):
    def __init__(self, n_entradas, n_classes):
        super().__init__()
        self.rede = nn.Sequential(
            nn.Linear(n_entradas, 32),
            nn.ReLU(),
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Linear(16, n_classes),
        )

    def forward(self, x):
        return self.rede(x)


modelo = RedeNeural(X_train.shape[1], len(set(y)))
criterio = nn.CrossEntropyLoss()
otimizador = optim.Adam(modelo.parameters(), lr=0.01)


# ------------------------------------------------------------------
# 3. Treino com validação + early stopping
# ------------------------------------------------------------------
epocas = 200
paciencia = 15  # quantas épocas esperar sem melhora antes de parar
melhor_perda_val = float("inf")
epocas_sem_melhora = 0
melhor_estado = None

for epoca in range(epocas):
    # --- passo de treino: aqui os pesos são atualizados ---
    modelo.train()
    otimizador.zero_grad()
    saida = modelo(X_train_t)
    perda_treino = criterio(saida, y_train_t)
    perda_treino.backward()
    otimizador.step()

    # --- passo de validação: só mede, nunca atualiza pesos ---
    modelo.eval()
    with torch.no_grad():
        saida_val = modelo(X_val_t)
        perda_val = criterio(saida_val, y_val_t).item()

    if (epoca + 1) % 10 == 0:
        print(f"Época {epoca + 1}: perda treino={perda_treino.item():.4f} | perda val={perda_val:.4f}")

    # --- early stopping: guarda o melhor modelo visto até agora ---
    if perda_val < melhor_perda_val:
        melhor_perda_val = perda_val
        melhor_estado = copy.deepcopy(modelo.state_dict())
        epocas_sem_melhora = 0
    else:
        epocas_sem_melhora += 1
        if epocas_sem_melhora >= paciencia:
            print(f"\nParando cedo na época {epoca + 1} (sem melhora na validação há {paciencia} épocas)")
            break

# Recarrega os pesos do melhor momento (menor perda de validação), não os últimos
modelo.load_state_dict(melhor_estado)


# ------------------------------------------------------------------
# 4. Avaliação final — só toca no teste uma única vez, no fim de tudo
# ------------------------------------------------------------------
modelo.eval()
with torch.no_grad():
    saida_teste = modelo(X_test_t)
    previsoes = torch.argmax(saida_teste, dim=1).numpy()

print("\nAcurácia no teste:", accuracy_score(y_test, previsoes))
print("\nRelatório de classificação:\n", classification_report(y_test, previsoes))