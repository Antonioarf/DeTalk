import pygame
import random
import time

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255,0,255)
CIANO= (0,255,255)
class LIVES(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, lives_img):

        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(lives_img, (80, 80))
       
        
#        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect() 
        
        # Sorteia um lugar inicial em x
        self.rect.left = 240
        # Sorteia um lugar inicial em y
        self.rect.bottom = 160  

        # Sorteia uma velocidade inicial
        self.speedx = 0
        self.speedy = 0
        
        # Melhora a colisÃ£o estabelecendo um raio de um circulo
        self.radius = int(self.rect.width * .85 / 2)
    
    def update(self):        
        # Se o tiro passar do inicio da tela, morre.
#        if self.rect.bottom < 0:
            #self.kill()
        def movimento_absoluto(self,eixoX, eixoY):
    #personagem.kill()
            self.rect.left += 80*eixoX 
            self.rect.bottom += 80*eixoX     
    # Metodo que atualiza a posiÃ§Ã£o do meteoro
        pass