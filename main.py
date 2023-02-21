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


# inicializar variáveis;

k = 1000

# Inicializar posicoes;


planeta = MassCenter(np.array([500,200]),25,'yellow',screen,k)
lua = MassCenter(np.array([500,300]),10,'blue',screen,k/2)
espaco = [planeta,lua]
espaco2 = [planeta]
goal = Goal(np.array([1100,400]),10,screen)

# Personagem;

personagem = CrocoBoy()
imagem = pygame.Surface((5, 5))  # Tamanho do personagem
imagem.fill(personagem.color)  # Cor do personagem
personagem.vel *= 100

# Inicializa Fases;

stage_1 = Stage(espaco,np.array([50,200]))
stage_2 = Stage(espaco2,np.array([100,250]))
# stage_3 = Stage()
# stage_4 = Stage()
# stage_5 = Stage()

stages = [stage_1,stage_2]
stage_index = 0
stage = stages[stage_index]

# Inicializa jogo

rodando = True

while rodando:
    stage = stages[stage_index]
    # Capturar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

        # if event.type == pygame: Level skip key
        #     stage_index += 1
        #     personagem.death(stage)

        if event.type == pygame.MOUSEBUTTONDOWN and personagem.vel[0] == 0 and personagem.vel[1] == 0:
            y = pygame.mouse.get_pos()
            yv = y - personagem.objs
            mv = np.linalg.norm(y)
        
            personagem.vel = 10*yv/mv
        
       

    if personagem.objs[0] < 10 or personagem.objs[0] > 1270 or personagem.objs[1] < 10 or personagem.objs[1] > 710: # Se eu chegar ao limite da tela, reinicio a posição do personagem
        personagem.death(stage)   


    collision_result = personagem.collide(espaco,goal)

    if collision_result == "FAILURE":
        personagem.death(stage)
    elif collision_result == "SUCCESS":
        stage_index += 1

    # Controlar frame rate
    clock.tick(FPS)

    # Processar posicoes
        
    if personagem.vel[0] != 0 and personagem.vel[1] != 0:
        a = 0
        for corpo_celeste in espaco:
            '''
            dp = planeta - personagem.objs
            d = np.linalg.norm(dp)
            a = (dp/d)*k/d**2
            '''
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
    goal.draw()

    # Update!
    pygame.display.update()

# Terminar tela
pygame.quit()