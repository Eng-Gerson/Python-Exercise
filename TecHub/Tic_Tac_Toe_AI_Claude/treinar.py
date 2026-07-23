"""
Treina a rede neural com o dataset de jogo da velha (train / validação /
teste, com early stopping) e guarda os pesos treinados, para serem
usados depois pelo jogo (jogar.py).

Uso:
    python dados/gerar_dataset.py   # só precisa de ser feito uma vez
    python treinar.py
"""

import copy
import os

import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

from modelo.rede_neural import RedeJogoDaVelha

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAMINHO_DATASET = os.path.join(BASE_DIR, "dados", "dataset_tic_tac_toe.csv")
CAMINHO_MODELO = os.path.join(BASE_DIR, "modelo", "modelo_treinado.pt")


def carregar_dados():
    if not os.path.exists(CAMINHO_DATASET):
        raise FileNotFoundError(
            f"Não encontrei '{CAMINHO_DATASET}'.\n"
            "Corre primeiro:\n"
            "    python dados/gerar_dataset.py"
        )

    df = pd.read_csv(CAMINHO_DATASET)
    X = df[[f"c{i}" for i in range(9)]].values.astype("float32")
    y = df["melhor_jogada"].values.astype("int64")
    return X, y


def dividir_treino_val_teste(X, y):
    # 70% treino / 15% validação / 15% teste
    X_temp, X_teste, y_temp, y_teste = train_test_split(
        X, y, test_size=0.15, random_state=42, stratify=y
    )
    X_treino, X_val, y_treino, y_val = train_test_split(
        X_temp, y_temp, test_size=0.1765, random_state=42, stratify=y_temp
    )
    return X_treino, X_val, X_teste, y_treino, y_val, y_teste


def treinar():
    torch.manual_seed(42)

    X, y = carregar_dados()
    X_treino, X_val, X_teste, y_treino, y_val, y_teste = dividir_treino_val_teste(X, y)

    print(f"Treino: {len(X_treino)} | Validação: {len(X_val)} | Teste: {len(X_teste)}")

    X_treino_t = torch.tensor(X_treino)
    y_treino_t = torch.tensor(y_treino)
    X_val_t = torch.tensor(X_val)
    y_val_t = torch.tensor(y_val)
    X_teste_t = torch.tensor(X_teste)

    modelo = RedeJogoDaVelha()
    criterio = nn.CrossEntropyLoss()
    otimizador = optim.Adam(modelo.parameters(), lr=0.001)

    epocas = 300
    paciencia = 20
    melhor_perda_val = float("inf")
    epocas_sem_melhora = 0
    melhor_estado = None

    for epoca in range(epocas):
        # --- treino ---
        modelo.train()
        otimizador.zero_grad()
        saida = modelo(X_treino_t)
        perda_treino = criterio(saida, y_treino_t)
        perda_treino.backward()
        otimizador.step()

        # --- validação (nunca atualiza pesos) ---
        modelo.eval()
        with torch.no_grad():
            saida_val = modelo(X_val_t)
            perda_val = criterio(saida_val, y_val_t).item()

        if (epoca + 1) % 20 == 0:
            print(
                f"Época {epoca + 1}: perda treino={perda_treino.item():.4f} "
                f"| perda val={perda_val:.4f}"
            )

        # --- early stopping ---
        if perda_val < melhor_perda_val:
            melhor_perda_val = perda_val
            melhor_estado = copy.deepcopy(modelo.state_dict())
            epocas_sem_melhora = 0
        else:
            epocas_sem_melhora += 1
            if epocas_sem_melhora >= paciencia:
                print(
                    f"\nParando cedo na época {epoca + 1} "
                    f"(sem melhora na validação há {paciencia} épocas)"
                )
                break

    modelo.load_state_dict(melhor_estado)

    # --- avaliação final: só toca no teste uma vez, no fim ---
    modelo.eval()
    with torch.no_grad():
        saida_teste = modelo(X_teste_t)
        previsoes = torch.argmax(saida_teste, dim=1).numpy()

    print("\nAcurácia no teste (jogada prevista == jogada ótima do minimax):")
    print(round(accuracy_score(y_teste, previsoes), 4))
    print("\nRelatório de classificação:\n")
    print(classification_report(y_teste, previsoes, zero_division=0))

    os.makedirs(os.path.dirname(CAMINHO_MODELO), exist_ok=True)
    torch.save(modelo.state_dict(), CAMINHO_MODELO)
    print(f"Modelo guardado em '{CAMINHO_MODELO}'")


if __name__ == "__main__":
    treinar()
