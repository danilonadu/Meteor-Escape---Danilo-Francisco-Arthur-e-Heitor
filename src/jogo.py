import pygame
import random

from src.config import (
LARGURA_TELA,
ALTURA_TELA,
FPS,
TITULO_JOGO,
PRETO,
)

def executar_jogo():

    pygame.init()

    imagem_nave = pygame.image.load("assets/imagens/nave.png")
    imagem_meteoro = pygame.image.load("assets/imagens/meteoro.png")
    imagem_fundo = pygame.image.load("assets/imagens/fundo.png")

    imagem_nave = pygame.transform.scale(imagem_nave, (50, 50))
    imagem_meteoro = pygame.transform.scale(imagem_meteoro, (40, 40))
    imagem_fundo = pygame.transform.scale(
        imagem_fundo,
        (LARGURA_TELA, ALTURA_TELA)
    )

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()

    nave = pygame.Rect(
        LARGURA_TELA // 2 - 25,
        ALTURA_TELA - 80,
        50,
        50
    )

    meteoros = []

    pontos = 0

    fonte = pygame.font.SysFont(None, 36)

    rodando = True

    while rodando:

        relogio.tick(FPS)

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                rodando = False

        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_LEFT]:
            nave.x -= 6

        if teclas[pygame.K_RIGHT]:
            nave.x += 6

        if teclas[pygame.K_UP]:
            nave.y -= 6

        if teclas[pygame.K_DOWN]:
            nave.y += 6

        if nave.top < 0:
            nave.top = 0

        if nave.bottom > ALTURA_TELA:
            nave.bottom = ALTURA_TELA
            
        if nave.left < 0:
            nave.left = 0

        if nave.right > LARGURA_TELA:
            nave.right = LARGURA_TELA

        if random.randint(1, 40) == 1:

            meteoros.append(
                pygame.Rect(
                    random.randint(0, LARGURA_TELA - 30),
                    0,
                    30,
                    30
                )
            )

        for meteoro in meteoros[:]:

            meteoro.y += 5

            if meteoro.y > ALTURA_TELA:

                meteoros.remove(meteoro)
                pontos += 1

            elif nave.colliderect(meteoro):

                rodando = False

        tela.blit(imagem_fundo, (0, 0))

        tela.blit(imagem_nave, nave)

        for meteoro in meteoros:

            tela.blit(imagem_meteoro, meteoro)

        texto = fonte.render(
            f"Pontos: {pontos}",
            True,
            (255, 255, 255)
        )

        tela.blit(texto, (10, 10))

        pygame.display.flip()

    pygame.quit()