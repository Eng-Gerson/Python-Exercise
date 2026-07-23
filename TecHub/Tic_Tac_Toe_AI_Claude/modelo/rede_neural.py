"""Rede neural (PyTorch) que aprende a escolher a melhor jogada
num tabuleiro de jogo da velha."""

import torch
import torch.nn as nn


class RedeJogoDaVelha(nn.Module):
    """Recebe o estado do tabuleiro (9 valores: -1, 0 ou 1) e devolve
    uma pontuação (logit) para cada uma das 9 casas -- quanto maior a
    pontuação, mais recomendada é aquela jogada."""

    def __init__(self, n_entradas=9, n_saidas=9, n_neuronios=64):
        super().__init__()
        self.rede = nn.Sequential(
            nn.Linear(n_entradas, n_neuronios),
            nn.ReLU(),
            nn.Linear(n_neuronios, n_neuronios),
            nn.ReLU(),
            nn.Linear(n_neuronios, n_saidas),
        )

    def forward(self, x):
        return self.rede(x)


def escolher_jogada(modelo, casas, jogadas_disponiveis):
    """Usa o modelo treinado para escolher a melhor jogada LEGAL para o
    estado atual do tabuleiro.

    casas               -- lista com 9 valores (-1, 0 ou 1)
    jogadas_disponiveis -- lista de índices (0-8) das casas vazias
    """
    modelo.eval()
    with torch.no_grad():
        entrada = torch.tensor([casas], dtype=torch.float32)
        saida = modelo(entrada).squeeze(0)

        # A rede pode "querer" jogar numa casa já ocupada -- isso é
        # bloqueado aqui, dando pontuação -infinito às casas ilegais,
        # para que o argmax só possa escolher entre as legais.
        mascara = torch.full((9,), float("-inf"))
        mascara[jogadas_disponiveis] = 0.0
        saida_legal = saida + mascara

        return int(torch.argmax(saida_legal).item())
