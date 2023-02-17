# Pacotes necessários.

import numpy as np
import pygame
from pygame.locals import *
from Classes import *

pygame.init()

# Tamanho da tela e definição do FPS

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
FPS = 60 

BLACK = (0, 0, 0)

planeta = np.array([300,200]) 
personagem = CrocoBoy()

# goal = Goal()

# Inicializar posicoes

personagem.objs = personagem.s0

k = 1000

a = np.array([0, 0.2])


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
        if event.type == pygame.MOUSEBUTTONDOWN and personagem.vel[0] == 0 and personagem.vel[1] == 0:
            y = pygame.mouse.get_pos()
            yv = y - personagem.objs
            mv = np.linalg.norm(y)
        
            personagem.vel = 10*yv/mv

    if personagem.objs[0] < 10 or personagem.objs[0]>1270 or personagem.objs[1]<10 or personagem.objs[1]>710: # Se eu chegar ao limite da tela, reinicio a posição do personagem
        personagem.reset()

    '''
    if personagem.objs[0] == goal.objs[0] and personagem.objs[0] == goal.objs[1]:
        pass
    '''        

    planeta1 = MassCenter(planeta,25,'yellow',screen,k)
    lua1 = MassCenter(lua,10,'blue',screen,k/2)
    espaco = [planeta1,lua1]

    # Controlar frame rate
    clock.tick(FPS)

    # Processar posicoes
    personagem.collide(espaco)
    if personagem.vel[0] != 0 and personagem.vel[1] != 0:
        a = 0
        for corpo_celeste in espaco:
            # dp = planeta - personagem.objs
            # d = np.linalg.norm(dp)
            # a = (dp/d)*k/d**2
            a += corpo_celeste.gravitational_force(personagem.objs)
        

        personagem.vel = personagem.vel + a 

    personagem.objs = personagem.objs + 0.1 * personagem.vel # s = s(-1) + a

    # Desenhar fundo
    screen.fill(BLACK)

    # Desenhar personagem
    rect = personagem.rect()  # First tuple is position, second is size.
    screen.blit(imagem, rect)

    # Obstacles
    for corpo_celeste in espaco:
        corpo_celeste.draw()

    # Update!
    pygame.display.update()

# Terminar tela
pygame.quit()