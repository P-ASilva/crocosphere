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

# Inicializar Sprites;

sprites = {
    'bola': pygame.image.load('croco-game/assets/sprites/bola_smol.png'),
    'bg': pygame.image.load('croco-game/assets/sprites/bg.jpg'),
    'planet': pygame.image.load('croco-game/assets/sprites/planet.png'),
    'target': pygame.image.load('croco-game/assets/sprites/target.png'),
    'lua': pygame.image.load('croco-game/assets/sprites/lua.png'),
    'sol': pygame.image.load('croco-game/assets/sprites/sol.png'),
    'win': pygame.image.load('croco-game/assets/sprites/win.png'),
}


# Inicializar posicoes;

goal_1 = Goal(np.array([1100,400]),10,screen)
goal_2 = Goal(np.array([1050,150]),10,screen)
goal_3 = Goal(np.array([900,400]),10,screen)
goal_4 = Goal(np.array([1300,800]),10,screen)
goals = [goal_1,goal_2,goal_3, goal_4]

planeta_1 = MassCenter(np.array([750,300]),25,'purple', 'planet', screen)
lua_1 = MassCenter(np.array([780,250]),10,'blue', 'lua', screen)
espaco_1 = [planeta_1,lua_1]

planeta_2 = MassCenter(np.array([650,300]),25,'purple', 'planet', screen)
lua_2 = MassCenter(np.array([680,250]),10,'blue', 'lua', screen)
planeta_3 = MassCenter(np.array([700,600]),100,'pink', 'planet', screen)
espaco_2 = [planeta_2,lua_2,planeta_3]

sol = MassCenter(np.array([0,0]),500,'red','sol', screen)
planeta_4 = MassCenter(np.array([800,250]),100,'pink', 'planet', screen)
lua_3 = MassCenter(np.array([560,450]),20,'blue', 'lua', screen)
espaco_3 = [sol,planeta_4,lua_3]

win = MassCenter(np.array([0,0]), 0, 'red', 'win', screen)
espaco_4 = [win]

# Personagem;

personagem = CrocoBoy()

# Inicializa Fases;

stage_1 = Stage(espaco_1,np.array([100,250]))
stage_2 = Stage(espaco_2,np.array([320,360])) 
stage_3 = Stage(espaco_3,np.array([400,600]))
stage_4 = Stage(espaco_4,np.array([0,0]))

stages = [stage_1,stage_2,stage_3, stage_4]
stage_index = 2
stage = stages[stage_index]

# Inicializa jogo;

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
    bgrect = pygame.Rect([0,0], [1280,720])
    screen.blit(sprites['bg'], bgrect)

    # Desenhar personagem
    rect = personagem.rect()
    screen.blit(sprites['bola'], rect)

    # Desenhar obstaculos
    for corpo_celeste in stage.planetas:
        if corpo_celeste.type == 'planet':
            planet = pygame.transform.scale(sprites['planet'], (corpo_celeste.radius*8, corpo_celeste.radius*8))
            screen.blit(planet, (corpo_celeste.center[0]-4*corpo_celeste.radius,corpo_celeste.center[1]-4*corpo_celeste.radius))
        elif corpo_celeste.type == 'lua':
            planet = pygame.transform.scale(sprites['lua'], (corpo_celeste.radius*8, corpo_celeste.radius*8))
            screen.blit(planet, (corpo_celeste.center[0]-4*corpo_celeste.radius,corpo_celeste.center[1]-4*corpo_celeste.radius))
        elif corpo_celeste.type == 'sol':
            planet = pygame.transform.scale(sprites['sol'], (corpo_celeste.radius*4, corpo_celeste.radius*4))
            screen.blit(planet, (corpo_celeste.center[0]-2.4*corpo_celeste.radius,corpo_celeste.center[1]-2.4*corpo_celeste.radius))
        elif corpo_celeste.type == 'win':
            planet = pygame.transform.scale(sprites['win'], (1280, 720))
            screen.blit(planet, (0, 0))
    
    # Desenhar objetivo
    screen.blit(sprites['target'], ((goals[stage_index].center[0] - goals[stage_index].radius), (goals[stage_index].center[1] - goals[stage_index].radius)))

    # Update!
    pygame.display.update()

# Terminar tela
pygame.quit()