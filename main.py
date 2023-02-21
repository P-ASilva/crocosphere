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

k = 2000

# Inicializar posicoes;
goal_1 = Goal(np.array([1100,400]),10,screen)
goal_2 = Goal(np.array([600,50]),10,screen)
goals = [goal_1,goal_1,goal_2]

planeta = MassCenter(np.array([750,300]),25,'purple',screen,k)
lua = MassCenter(np.array([750,400]),10,'blue',screen,k/2)
espaco = [planeta,lua]
espaco2 = [planeta]
sol = MassCenter(np.array([0,0]),500,'red',screen,k*150)
espaco3 = [sol]


# Personagem;

personagem = CrocoBoy()
imagem = pygame.Surface((personagem.size, personagem.size))  # Tamanho do personagem
imagem.fill(personagem.color)  # Cor do personagem

# Inicializa Fases;

stage_1 = Stage(espaco2,np.array([100,250]))
stage_2 = Stage(espaco,np.array([320,360])) 
stage_3 = Stage(espaco3,np.array([400,600]))
stage_4 = Stage(espaco2,np.array([100,250]))
stage_5 = Stage(espaco2,np.array([100,250]))

stages = [stage_1,stage_2,stage_3,stage_4,stage_5]
stage_index = 0
stage = stages[stage_index]

# Inicializa jogo

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
        
            personagem.vel = 90*yv/mv
        
    # Captura de colisão
    collision_result = personagem.collide(stage.planetas,goals[stage_index])

    if collision_result == "FAILURE":
        personagem.death(stage)
    elif collision_result == "SUCCESS":     
        stage_index += 1
        if stage_index < len(stages):
            stage = stages[stage_index]
        personagem.death(stage)

    # Controlar frame rate
    clock.tick(FPS)

    # Processar posicoes
        

    if personagem.vel[0] != 0 and personagem.vel[1] != 0:
        a = 0
        for corpo_celeste in stage.planetas: # Somatória das forças em efeito
            a += personagem.em_orbita(corpo_celeste)
        
        personagem.vel = personagem.vel + a 

    personagem.objs = personagem.objs + 0.1 * personagem.vel # s = s(-1) + mod*a

    # Desenhar fundo
    screen.fill(BLACK)

    # Desenhar personagem
    rect = personagem.rect()  # First tuple is position, second is size.
    screen.blit(imagem, rect)

    # Obstacles
    for corpo_celeste in stage.planetas:
        corpo_celeste.draw()
    goals[stage_index].draw()

    # Update!
    pygame.display.update()

# Terminar tela
pygame.quit()