import pygame
import random

from src.config import (
LARGURA_TELA,
ALTURA_TELA,
FPS,
TITULO_JOGO,
PRETO,
)

from src.dados import carregar_recorde, salvar_recorde

def executar_jogo():

    #INICIAR JOGO
    pygame.init()

    #INICIAR SONS
    pygame.mixer.init()

    #COLOCAR FONTE NOS TEXTOS
    fonte_titulo = pygame.font.Font(
        "assets/fontes/PressStart2P.ttf",
        32
    )
    fonte_menu = pygame.font.Font(
        "assets/fontes/PressStart2P.ttf",
        16
    )

    #CARREGAR IMAGENS
    imagem_nave = pygame.image.load("assets/imagens/nave.png")
    imagem_nave_propulsao = pygame.image.load(
    "assets/imagens/nave_propulsao.png"
    )
    imagem_meteoro = pygame.image.load("assets/imagens/meteoro.png")
    imagem_fundo = pygame.image.load("assets/imagens/fundo.png")

    coracao_cheio = pygame.image.load(
        "assets/imagens/Coracao Cheio.png"
    )

    coracao_vazio = pygame.image.load(
        "assets/imagens/Coracao Vazio.png"
    )

    #CARREGAR SONS
    som_colisao = pygame.mixer.Sound(
        "assets/sons/colisao.wav"
    )

    som_vitoria = pygame.mixer.Sound(
        "assets/sons/vitoria.wav"
    )

    som_gameover = pygame.mixer.Sound(
        "assets/sons/gameover.wav"
    )

    som_bip = pygame.mixer.Sound(
        "assets/sons/bip.wav"
    )

    pygame.mixer.music.load(
        "assets/sons/backgroundmusic.wav"
    )

    pygame.mixer.music.set_volume(0.3)

    pygame.mixer.music.play(-1)

    #TAMANHO DAS IMAGENS
    imagem_nave = pygame.transform.scale(imagem_nave, (50, 50))
    imagem_nave_propulsao = pygame.transform.scale(
    imagem_nave_propulsao,
    (50, 50)
    )
    imagem_meteoro = pygame.transform.scale(imagem_meteoro, (40, 40))
    imagem_fundo = pygame.transform.scale(
        imagem_fundo,
        (LARGURA_TELA, ALTURA_TELA)
    )

    coracao_cheio = pygame.transform.scale(
        coracao_cheio,
        (32, 32)
    )

    coracao_vazio = pygame.transform.scale(
        coracao_vazio,
        (32, 32)
    )

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    modo_jogo = "recorde"
    modo_escolhido = False

    dificuldade_escolhida = False
    velocidade_meteoro = 9

    #LOOP DE SELEÇÃO DE MODO
    while not modo_escolhido:

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                pygame.quit()
                return

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_1:
                    som_bip.play()
                    modo_jogo = "recorde"
                    modo_escolhido = True

                elif evento.key == pygame.K_2:
                    som_bip.play()
                    modo_jogo = "vitoria"
                    modo_escolhido = True

        tela.blit(imagem_fundo, (0, 0))

        titulo = fonte_titulo.render(
            "METEOR ESCAPE",
            True,
            (255, 255, 255)
        )

        subtitulo = fonte_menu.render(
            "Escolha o modo",
            True,
            (255, 255, 255)
        )

        recorde = fonte_menu.render(
            "1 - Recorde",
            True,
            (255, 255, 255)
        )

        vitoria_texto = fonte_menu.render(
            "2 - Vitoria",
            True,
            (255, 255, 255)
        )

        tela.blit(
            titulo,
            ((LARGURA_TELA - titulo.get_width()) // 2, 150)
        )

        tela.blit(
            subtitulo,
            ((LARGURA_TELA - subtitulo.get_width()) // 2, 250)
        )

        tela.blit(
            recorde,
            ((LARGURA_TELA - recorde.get_width()) // 2, 330)
        )

        tela.blit(
            vitoria_texto,
            ((LARGURA_TELA - vitoria_texto.get_width()) // 2, 380)
        )

        pygame.display.flip()

    #LOOP DE SELEÇÃO DE DIFICULDADE
    while not dificuldade_escolhida:

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                pygame.quit()
                return

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_1:
                    som_bip.play()
                    velocidade_meteoro = 6
                    dificuldade_escolhida = True

                elif evento.key == pygame.K_2:
                    som_bip.play()
                    velocidade_meteoro = 9
                    dificuldade_escolhida = True

                elif evento.key == pygame.K_3:
                    som_bip.play()
                    velocidade_meteoro = 12
                    dificuldade_escolhida = True

        tela.blit(imagem_fundo, (0, 0))

        titulo = fonte_titulo.render(
            "METEOR ESCAPE",
            True,
            (255, 255, 255)
        )

        subtitulo = fonte_menu.render(
            "Escolha a dificuldade",
            True,
            (255, 255, 255)
        )

        facil = fonte_menu.render(
            "1 - Facil",
            True,
            (255, 255, 255)
        )

        normal = fonte_menu.render(
            "2 - Normal",
            True,
            (255, 255, 255)
        )

        dificil = fonte_menu.render(
            "3 - Dificil",
            True,
            (255, 255, 255)
        )

        tela.blit(
            titulo,
            ((LARGURA_TELA - titulo.get_width()) // 2, 150)
        )

        tela.blit(
            subtitulo,
            ((LARGURA_TELA - subtitulo.get_width()) // 2, 250)
        )

        tela.blit(
            facil,
            ((LARGURA_TELA - facil.get_width()) // 2, 330)
        )

        tela.blit(
            normal,
            ((LARGURA_TELA - normal.get_width()) // 2, 380)
        )

        tela.blit(
            dificil,
            ((LARGURA_TELA - dificil.get_width()) // 2, 430)
        )

        pygame.display.flip()

    #MÚSICA DO MENU PARA
    pygame.mixer.music.stop()

    #MÚSICA DE GAMEPLAY COMEÇA
    pygame.mixer.music.load(
        "assets/sons/gameplaymusic.wav"
    )

    pygame.mixer.music.set_volume(0.2)

    pygame.mixer.music.play(-1)

    relogio = pygame.time.Clock()

    nave = pygame.Rect(
        LARGURA_TELA // 2 - 25,
        ALTURA_TELA - 80,
        50,
        50
    )

    meteoros = []

    pontos = 0
    vidas = 3
    recorde = carregar_recorde("data/recorde.txt")

    fonte = pygame.font.Font(
        "assets/fontes/PressStart2P.ttf",
        16
    )

    rodando = True

    game_over = False
    vitoria = False

    #LOOP PRINCIPAL
    while rodando:

        relogio.tick(FPS)

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                rodando = False

        teclas = pygame.key.get_pressed()

        #NAVE MOVIMENTAR QUANDO TECLAS PRESSIONADAS
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            nave.x -= 6

        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            nave.x += 6

        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            nave.y -= 6

        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            nave.y += 6

        if nave.top < 0:
            nave.top = 0

        if nave.bottom > ALTURA_TELA:
            nave.bottom = ALTURA_TELA
            
        if nave.left < 0:
            nave.left = 0

        if nave.right > LARGURA_TELA:
            nave.right = LARGURA_TELA

        #INCIDENCIA DE METEOROS
        chance_spawn = 25

        if velocidade_meteoro == 9:
            chance_spawn = 15

        elif velocidade_meteoro == 12:
            chance_spawn = 8

        if random.randint(1, chance_spawn) == 1:

            meteoros.append(
                pygame.Rect(
                    random.randint(0, LARGURA_TELA - 30),
                    0,
                    30,
                    30
                )
            )

        for meteoro in meteoros[:]:

            meteoro.y += velocidade_meteoro

            if meteoro.y > ALTURA_TELA:

                meteoros.remove(meteoro)
                pontos += 1

            elif nave.colliderect(meteoro):
                
                som_colisao.play()
                
                meteoros.remove(meteoro)

                vidas -= 1

                if vidas <= 0:

                    som_gameover.play()

                    pygame.mixer.music.stop()

                    pygame.mixer.music.load(
                        "assets/sons/backgroundmusic.wav"
                    )

                    pygame.mixer.music.play(-1)

                    game_over = True
                    rodando = False

        if modo_jogo == "recorde":

            if pontos > recorde:

                recorde = pontos

                salvar_recorde(
                    "data/recorde.txt",
                    recorde
                )

        if modo_jogo == "vitoria":

            if pontos >= 100:

                som_vitoria.play()

                pygame.mixer.music.stop()

                pygame.mixer.music.load(
                    "assets/sons/backgroundmusic.wav"
                )

                pygame.mixer.music.play(-1)

                vitoria = True
                rodando = False

        tela.blit(imagem_fundo, (0, 0))

        if teclas[pygame.K_w] or teclas[pygame.K_UP]:
            tela.blit(imagem_nave_propulsao, nave)
        else:
            tela.blit(imagem_nave, nave)

        for meteoro in meteoros:

            tela.blit(imagem_meteoro, meteoro)

        texto_pontos = fonte.render(
            f"Pontos: {pontos}",
            True,
            (255, 255, 255)
        )

        tela.blit(texto_pontos, (10, 10))

        #CORAÇÕES CHEIOS E VAZIOS
        inicio_coracoes = (
            LARGURA_TELA // 2
        ) - 50

        for i in range(3):

            if i < vidas:

                tela.blit(
                    coracao_cheio,
                    (
                        inicio_coracoes + i * 35,
                        5
                    )
                )

            else:

                tela.blit(
                    coracao_vazio,
                    (
                        inicio_coracoes + i * 35,
                        5
                    )
                )

        #SE FOR NO MODO RECORDE, MOSTRA O TEXTO DE RECORDE
        if modo_jogo == "recorde":

            texto_recorde = fonte.render(
                f"Recorde: {recorde}",
                True,
                (255, 255, 255)
            )

            recorde_x = (
                LARGURA_TELA
                - texto_recorde.get_width()
                - 10
            )

            tela.blit(texto_recorde, (recorde_x, 10))

        #SE FIR NO MODO VITÓRIA, MOSTRA O TEXTO DE META
        else:

            texto_meta = fonte.render(
                "Meta: 100",
                True,
                (255, 255, 255)
            )

            meta_x = (
                LARGURA_TELA
                - texto_meta.get_width()
                - 10
            )

            tela.blit(texto_meta, (meta_x, 10))

        pygame.display.flip()

    #LOOP PRO GAME OVER (QUANDO PERDE)
    while game_over:

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                pygame.quit()
                return

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_r:
                    som_bip.play()
                    pygame.time.delay(150)
                    executar_jogo()
                    return

        tela.blit(imagem_fundo, (0, 0))

        texto1 = fonte_titulo.render(
            "GAME OVER",
            True,
            (255, 0, 0)
        )

        texto2 = fonte_menu.render(
            f"Pontos: {pontos}",
            True,
            (255, 255, 255)
        )

        texto3 = fonte_menu.render(
            "Pressione R",
            True,
            (255, 255, 255)
        )

        tela.blit(
            texto1,
            ((LARGURA_TELA - texto1.get_width()) // 2, 200)
        )

        tela.blit(
            texto2,
            ((LARGURA_TELA - texto2.get_width()) // 2, 300)
        )

        tela.blit(
            texto3,
            ((LARGURA_TELA - texto3.get_width()) // 2, 380)
        )

        pygame.display.flip()

    #LOOP PRA VITÓRIA (QUANDO GANHA)
    while vitoria:

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                pygame.quit()
                return

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_r:
                    som_bip.play()
                    pygame.time.delay(150)
                    executar_jogo()
                    return

        tela.blit(imagem_fundo, (0, 0))

        texto1 = fonte_titulo.render(
            "VOCE VENCEU!",
            True,
            (0, 255, 0)
        )

        texto2 = fonte_menu.render(
            f"Pontos: {pontos}",
            True,
            (255, 255, 255)
        )

        texto3 = fonte_menu.render(
            "Pressione R",
            True,
            (255, 255, 255)
        )

        tela.blit(
            texto1,
            ((LARGURA_TELA - texto1.get_width()) // 2, 200)
        )

        tela.blit(
            texto2,
            ((LARGURA_TELA - texto2.get_width()) // 2, 300)
        )

        tela.blit(
            texto3,
            ((LARGURA_TELA - texto3.get_width()) // 2, 380)
        )

        pygame.display.flip()

    pygame.quit()