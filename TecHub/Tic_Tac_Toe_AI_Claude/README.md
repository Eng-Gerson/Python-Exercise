# Jogo da Velha com IA (PyTorch)

Projeto em Python com três partes:

1. **O jogo** (`jogo/tabuleiro.py`) — lógica pura do jogo da velha (tabuleiro, jogadas, verificação de vencedor).
2. **A rede neural** (`modelo/rede_neural.py`) — uma rede em PyTorch que aprende a escolher a melhor jogada para um tabuleiro dado.
3. **O treino e a integração** (`treinar.py` e `jogar.py`) — treina a rede com um dataset gerado por minimax e depois usa o modelo treinado como adversário no jogo.

## Estrutura

```
tic_tac_toe_ia/
├── requirements.txt
├── jogo/
│   ├── __init__.py
│   └── tabuleiro.py        # Lógica do jogo (tabuleiro, jogadas, vencedor)
├── dados/
│   └── gerar_dataset.py    # Gera o dataset via minimax (estado -> melhor jogada)
├── modelo/
│   ├── __init__.py
│   ├── rede_neural.py      # Definição da rede neural + função de escolher jogada
│   └── modelo_treinado.pt  # Pesos treinados (criado depois de correr treinar.py)
├── treinar.py               # Treina a rede (train/validação/teste + early stopping)
└── jogar.py                  # Joga contra a rede treinada, no terminal
```

## Como usar

### 1. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 2. Gerar o dataset

Como o jogo da velha tem um número pequeno de estados possíveis, o dataset é gerado por força bruta: simula-se todas as partidas legais e usa-se o algoritmo **minimax** para calcular qual é a jogada ótima em cada estado (assumindo que os dois jogadores jogam sempre da melhor forma possível).

```bash
python dados/gerar_dataset.py
```

Isto cria `dados/dataset_tic_tac_toe.csv` com ~4500 linhas: 9 colunas para o estado do tabuleiro (`-1` = O, `0` = vazio, `1` = X) e uma coluna `melhor_jogada` (0 a 8) com a jogada recomendada.

### 3. Treinar a rede neural

```bash
python treinar.py
```

O script divide o dataset em treino (70%), validação (15%) e teste (15%), treina com `CrossEntropyLoss` + Adam, usa **early stopping** baseado na perda de validação (evita overfitting), e no fim mostra a acurácia no conjunto de teste. Os pesos treinados ficam guardados em `modelo/modelo_treinado.pt`.

### 4. Jogar contra a IA

```bash
python jogar.py
```

Escolhe se queres jogar com X (começas tu) ou O (a IA começa), e joga no terminal indicando o número da casa (1 a 9). A IA usa o modelo treinado para escolher a jogada com a maior pontuação entre as casas ainda disponíveis.

> Se corrmes `jogar.py` sem ter treinado o modelo primeiro, o jogo ainda funciona, mas a IA joga com pesos aleatórios (vai jogar mal) — o script avisa isso no início.

## Notas

- A acurácia no teste mede se a rede escolheu **exatamente** a mesma jogada que o minimax indicou como ótima. Em alguns estados existe mais que uma jogada igualmente boa, mas o dataset só guarda uma — por isso a acurácia real "jogando bem" costuma ser mais alta do que esse número sozinho sugere.
- Não há validação de entradas mais rigorosa no `jogar.py` (por exemplo, tratar todos os casos de entrada inválida) — é um projeto simples focado em mostrar o jogo, o dataset e o treino integrados.
