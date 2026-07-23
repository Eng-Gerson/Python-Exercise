"""Lógica do jogo da velha (tic-tac-toe).

O tabuleiro é representado por uma lista de 9 posições:
    0  -> casa vazia
    1  -> casa ocupada por X
   -1  -> casa ocupada por O

As posições são numeradas de 0 a 8, da esquerda para a direita e de
cima para baixo:

     0 | 1 | 2
    -----------
     3 | 4 | 5
    -----------
     6 | 7 | 8
"""

VAZIO, X, O = 0, 1, -1

LINHAS_VENCEDORAS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # linhas
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # colunas
    (0, 4, 8), (2, 4, 6),             # diagonais
]


class Tabuleiro:
    """Representa o estado de uma partida de jogo da velha."""

    def __init__(self, casas=None):
        self.casas = list(casas) if casas is not None else [VAZIO] * 9

    def copia(self):
        return Tabuleiro(self.casas)

    def jogadas_disponiveis(self):
        return [i for i, v in enumerate(self.casas) if v == VAZIO]

    def fazer_jogada(self, posicao, jogador):
        if self.casas[posicao] != VAZIO:
            raise ValueError(f"A casa {posicao} já está ocupada.")
        self.casas[posicao] = jogador

    def jogador_da_vez(self):
        """X joga sempre primeiro, depois alternam."""
        n_jogadas = sum(1 for v in self.casas if v != VAZIO)
        return X if n_jogadas % 2 == 0 else O

    def vencedor(self):
        """Devolve X, O, ou None se ainda não há vencedor."""
        for a, b, c in LINHAS_VENCEDORAS:
            soma = self.casas[a] + self.casas[b] + self.casas[c]
            if soma == 3:
                return X
            if soma == -3:
                return O
        return None

    def cheio(self):
        return VAZIO not in self.casas

    def fim_de_jogo(self):
        return self.vencedor() is not None or self.cheio()

    def imprimir(self):
        simbolos = {VAZIO: " ", X: "X", O: "O"}
        linhas = []
        for linha in range(3):
            casas_linha = self.casas[linha * 3:(linha + 1) * 3]
            linhas.append(" | ".join(simbolos[c] for c in casas_linha))
        print(("\n" + "-" * 9 + "\n").join(linhas))
