# Pacotes necessários.

import matplotlib.pyplot as plt
import numpy as np
import pygame
import random
from pygame.locals import *

class CrocoBoy():
    def __init__(self) -> None:
        self.color = (30, 200, 20)
        self.vel = np.array([0,0])
        self.s0 = np.array([50,200])
        self.objs = self.s0
        
    def reset(self):
        self.objs, self.vel = self.s0, np.array([0,0])

class MassCenter():
    def __init__(self,x,y,g):
        self.center = np.array(x,y)
        self.g = g


class Stage1():
    def __init__(self):
        pass

    def endstage(self):
        pass

class Stage2():
    def __init__(self):
        pass
    
    def endstage(self):
        pass

pygame.init()

# Tamanho da tela e definição do FPS

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
FPS = 60 

BLACK = (0, 0, 0)

personagem = CrocoBoy()

# Inicializar posicoes

personagem.objs = personagem.s0

k = 1000

a = np.array([0, 0.2])

planeta = np.array([300,200]) 
lua = np.array([300,250])

# Personagem
imagem = pygame.Surface((5, 5))  # Tamanho do personagem
imagem.fill(personagem.color)  # Cor do personagem

rodando = True

while rodando:
    # Capturar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('click')
            y = pygame.mouse.get_pos()
            yv = y - personagem.objs
            mv = np.linalg.norm(y)
        
            personagem.vel = 5*yv/mv

    if personagem.objs[0] < 10 or personagem.objs[0]>1270 or personagem.objs[1]<10 or personagem.objs[1]>710: # Se eu chegar ao limite da tela, reinicio a posição do personagem
        personagem.reset()
        

    # Controlar frame rate
    clock.tick(FPS)

    # Processar posicoes


    if personagem.vel[0] != 0 and personagem.vel[1] != 0:
        
        dp = planeta - personagem.objs
        d = np.linalg.norm(dp) # modulo1
        a = (dp/d)*k/d**2

        dp = lua - personagem.objs
        d = np.linalg.norm(dp) # modulo2
        a2 = (dp/d)*(k/2)/d**2

        personagem.vel = personagem.vel + a + a2

    personagem.objs = personagem.objs + 0.1 * personagem.vel # s = s(-1) + a

    # Desenhar fundo
    screen.fill(BLACK)

    # Desenhar personagem
    rect = pygame.Rect(personagem.objs, (10, 10))  # First tuple is position, second is size.
    screen.blit(imagem, rect)

    # Obstacles
    circle = pygame.draw.circle(surface = screen, radius = 25,center=planeta,color='yellow')
    circle2 = pygame.draw.circle(surface = screen, radius = 10,center=lua,color='blue')

    # Update!
    pygame.display.update()

# Terminar tela
pygame.quit()