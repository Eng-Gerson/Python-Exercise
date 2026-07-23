"""
Gera um dataset completo de jogo da velha: para cada configuração de
tabuleiro legal e não terminal, calcula (via minimax) qual é a jogada
ótima para quem tem a vez naquele momento.

Como o jogo da velha tem um número pequeno de estados possíveis, dá
para gerar o dataset inteiro por força bruta, sem depender de nenhum
dataset externo.

Uso:
    python dados/gerar_dataset.py
"""

import csv
import os
import sys

# Garante que o pacote "jogo" é encontrado mesmo correndo este ficheiro
# diretamente de dentro da pasta dados/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from jogo.tabuleiro import Tabuleiro, X  # noqa: E402

CAMINHO_SAIDA_PADRAO = os.path.join(BASE_DIR, "dados", "dataset_tic_tac_toe.csv")

_memo_minimax = {}


def minimax(tabuleiro):
    """Devolve (pontuacao, melhor_jogada) para o estado atual, assumindo
    que os dois jogadores jogam sempre da melhor forma possível.

    Pontuação: +1 se X vence, -1 se O vence, 0 se empate.
    """
    chave = tuple(tabuleiro.casas)
    if chave in _memo_minimax:
        return _memo_minimax[chave]

    vencedor = tabuleiro.vencedor()
    if vencedor is not None:
        resultado = (vencedor, None)
        _memo_minimax[chave] = resultado
        return resultado

    if tabuleiro.cheio():
        resultado = (0, None)
        _memo_minimax[chave] = resultado
        return resultado

    jogador = tabuleiro.jogador_da_vez()
    maximizando = jogador == X
    melhor_pontuacao = -2 if maximizando else 2
    melhor_jogada = None

    for posicao in tabuleiro.jogadas_disponiveis():
        proximo = tabuleiro.copia()
        proximo.fazer_jogada(posicao, jogador)
        pontuacao, _ = minimax(proximo)

        if maximizando and pontuacao > melhor_pontuacao:
            melhor_pontuacao, melhor_jogada = pontuacao, posicao
        elif not maximizando and pontuacao < melhor_pontuacao:
            melhor_pontuacao, melhor_jogada = pontuacao, posicao

    resultado = (melhor_pontuacao, melhor_jogada)
    _memo_minimax[chave] = resultado
    return resultado


def gerar_estados_alcancaveis():
    """Enumera, por simulação recursiva, todos os estados de tabuleiro
    legais que podem aparecer numa partida real (a partir do tabuleiro
    vazio, seguindo sempre as regras do jogo)."""
    vistos = set()

    def visitar(tabuleiro):
        chave = tuple(tabuleiro.casas)
        if chave in vistos:
            return
        vistos.add(chave)

        if tabuleiro.fim_de_jogo():
            return

        jogador = tabuleiro.jogador_da_vez()
        for posicao in tabuleiro.jogadas_disponiveis():
            proximo = tabuleiro.copia()
            proximo.fazer_jogada(posicao, jogador)
            visitar(proximo)

    visitar(Tabuleiro())
    return vistos


def gerar_dataset(caminho_saida=CAMINHO_SAIDA_PADRAO):
    estados = gerar_estados_alcancaveis()
    linhas = []

    for chave in estados:
        tabuleiro = Tabuleiro(list(chave))
        if tabuleiro.fim_de_jogo():
            continue  # estado terminal: não há jogada para rotular

        _, melhor_jogada = minimax(tabuleiro)
        linhas.append(list(chave) + [melhor_jogada])

    colunas = [f"c{i}" for i in range(9)] + ["melhor_jogada"]

    os.makedirs(os.path.dirname(caminho_saida), exist_ok=True)
    with open(caminho_saida, "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(colunas)
        escritor.writerows(linhas)

    print(f"Dataset gerado com {len(linhas)} estados em '{caminho_saida}'")
    return caminho_saida


if __name__ == "__main__":
    gerar_dataset()
