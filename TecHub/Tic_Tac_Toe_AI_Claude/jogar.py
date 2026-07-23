"""
Joga jogo da velha contra a rede neural treinada.

Uso:
    python jogar.py
"""

import os

import torch

from jogo.tabuleiro import Tabuleiro, X, O
from modelo.rede_neural import RedeJogoDaVelha, escolher_jogada

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAMINHO_MODELO = os.path.join(BASE_DIR, "modelo", "modelo_treinado.pt")


def carregar_modelo():
    modelo = RedeJogoDaVelha()
    if os.path.exists(CAMINHO_MODELO):
        modelo.load_state_dict(torch.load(CAMINHO_MODELO, map_location="cpu"))
        print("Modelo treinado carregado.\n")
    else:
        print(
            "Aviso: não encontrei um modelo treinado em "
            f"'{CAMINHO_MODELO}'.\n"
            "A IA vai jogar com pesos aleatórios (ainda sem treino).\n"
            "Para treinar, corre primeiro:\n"
            "    python dados/gerar_dataset.py\n"
            "    python treinar.py\n"
        )
    modelo.eval()
    return modelo


def pedir_jogada_humano(tabuleiro):
    disponiveis = tabuleiro.jogadas_disponiveis()
    while True:
        entrada = input(
            f"A tua vez (escolhe uma casa entre {[p + 1 for p in disponiveis]}): "
        )
        try:
            posicao = int(entrada) - 1
        except ValueError:
            print("Digita um número entre 1 e 9.")
            continue
        if posicao not in disponiveis:
            print("Essa casa não está disponível.")
            continue
        return posicao


def jogar():
    modelo = carregar_modelo()

    print("Casas numeradas assim:\n")
    print(" 1 | 2 | 3 \n-----------\n 4 | 5 | 6 \n-----------\n 7 | 8 | 9 \n")

    escolha = input(
        "Queres jogar com X (jogas primeiro) ou O (a IA começa)? [X/O]: "
    ).strip().upper()
    humano = X if escolha != "O" else O

    tabuleiro = Tabuleiro()

    while not tabuleiro.fim_de_jogo():
        print()
        tabuleiro.imprimir()
        print()

        jogador_da_vez = tabuleiro.jogador_da_vez()

        if jogador_da_vez == humano:
            posicao = pedir_jogada_humano(tabuleiro)
        else:
            posicao = escolher_jogada(
                modelo, tabuleiro.casas, tabuleiro.jogadas_disponiveis()
            )
            print(f"A IA jogou na casa {posicao + 1}.")

        tabuleiro.fazer_jogada(posicao, jogador_da_vez)

    print()
    tabuleiro.imprimir()
    print()

    vencedor = tabuleiro.vencedor()
    if vencedor is None:
        print("Empate!")
    elif vencedor == humano:
        print("Ganhaste!")
    else:
        print("A IA ganhou!")


if __name__ == "__main__":
    jogar()
