# Nome do Jogo

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

Este repositório é um template para os grupos da disciplina. A proposta é começar com uma base funcional e evoluir o jogo ao longo do semestre.

## Integrantes do grupo

- Danilo Amaral Nadu
- Francisco Berutti
- Heitor Henrique Gonçalves
- Arthur Lopes de Paiva

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (loop, regras, sprites e dados).
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (recorde/ranking).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo proposta inicial.

## Descrição do jogo

Meteor Escape é um jogo de sobrevivência em estilo retrô no qual o jogador controla uma nave espacial e deve
desviar de meteoros que caem continuamente pela tela.

O jogo possui dois modos de jogo:

- Modo Recorde: o objetivo é sobreviver o máximo possível e alcançar a maior pontuação.
- Modo Vitória: o jogador deve sobreviver até atingir 100 pontos para vencer a partida.

Além disso, o jogo conta com sistema de vidas, seleção de dificuldade, recorde persistente em arquivo, telas
de vitória e derrota e interface inspirada em jogos clássicos de pixel art.

## Objetivo do jogador

Controlar a nave espacial evitando colisões com os meteoros.

No modo Recorde, o objetivo é alcançar a maior pontuação possível antes de perder todas as vidas.

No modo Vitória, o objetivo é sobreviver até atingir 100 pontos.

## Regras do jogo

- O jogador controla uma nave espacial.
- Meteoros surgem aleatoriamente e caem em direção à nave.
- Cada meteoro evitado aumenta a pontuação do jogador.
- Colidir com um meteoro reduz uma vida.
- O jogador inicia cada partida com 3 vidas.
- Quando as vidas chegam a zero, ocorre o Game Over.
- No modo Vitória, a partida termina quando o jogador alcança 100 pontos.
- No modo Recorde, a partida continua até que todas as vidas sejam perdidas.
- O recorde é salvo em arquivo e permanece armazenado entre diferentes execuções do jogo.
- O jogador pode reiniciar a partida após uma vitória ou derrota.

## Controles

Movimentação
- W ou Seta para cima: mover para cima
- S ou Seta para baixo: mover para baixo
- A ou Seta para esquerda: mover para esquerda
 -D ou Seta para direita: mover para direita

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/danilonadu/Meteor-Escape---Danilo-Francisco-Arthur-e-Heitor.git
cd (caminho até a pasta)\Meteor-Escape---Danilo-Francisco-Arthur-e-Heitor
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Checklist mínimo para entrega

- Preencher este README com nome final, descrição real, regras e controles do jogo.
- Atualizar `docs/proposta.MD` com a proposta do grupo.
- Garantir que o jogo executa com `python main.py`.
- Garantir que os testes passam com `pytest`.

## Observações para os alunos

- Mantenham o código organizado em módulos pequenos e com responsabilidade clara.
- Comentem partes importantes da lógica, principalmente regras do jogo.
- Registrem decisões técnicas no README do grupo ao longo do desenvolvimento.

## Referências 

### Fonte de texto

* Press Start 2P — Google Fonts

### Imagens

* Imagens da nave, meteoros, fundo e interface desenvolvidas e adaptadas durante o projeto com auxílio de ferramentas de inteligência artificial e edição pelos integrantes do grupo.

### Sons e músicas

* Inserir as referências dos arquivos utilizados, caso sejam adicionados na versão final.
