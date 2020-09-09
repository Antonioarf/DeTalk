import pygame
import random
import time


from os import path
from classes import LIVES
# Estabelece a pasta que contem as figuras e sons.
img_dir = path.join(path.dirname(__file__), 'Imagens')
snd_dir = path.join(path.dirname(__file__), 'Sons')
fnt_dir = path.join(path.dirname(__file__), 'font')

# Dados gerais do jogo.
WIDTH = 1000 # Largura da tela
HEIGHT = 700 # Altura da tela
FPS = 55 # Frames por segundo

# Define algumas variÃ¡veis com as cores bÃ¡sicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

INIT = 0
GAME = 1
QUIT = 2
FIM = 4

# InicializaÃ§Ã£o do Pygame.
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption("Pitfall")
#############################################################################################################

def init_screen(screen):
    # Carrega todos os assets uma vez sÃ³ e guarda em um dicionÃ¡rio
    # VariÃ¡vel para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial


    all_sprites = pygame.sprite.Group()   
    running = True
    while running:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        ass = pygame.image.load(path.join('', "coracao.png")).convert()
        l = LIVES(ass)
        all_sprites.add(l)
        all_sprites.draw(screen)
        # Processa os eventos (mouse, teclado, botÃ£o, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                state = GAME
                # running = False
        all_sprites.update()
        # A cada loop, redesenha o fundo e os sprites
        all_sprites.draw(screen)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state


# Comando para evitar travamentos.
try:
    state = INIT
    while state != QUIT:
        if state == INIT:
            state = init_screen(screen)
        elif state == GAME:
            state, tesouro = game_screen(screen)
        elif state == FIM:
            state = end_game(screen,tesouro)
        else:
            state = QUIT
finally:
    pygame.quit()