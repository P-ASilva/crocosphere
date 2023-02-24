import numpy as np
import pygame 

# Classe do personagem 

class CrocoBoy():
    def __init__(self):
        self.vel = np.array([0,0])
        self.objs = np.array([0,0])
        self.size = 12
    
    def rect(self): # Criado como referência para colisão.
        return pygame.Rect(self.objs, (self.size, self.size))
    
    def collide(self,objects,goal=None): # Verifica se houve colisão com o objetivo,planeta ou fim da tela.
        for object in objects:
            if ( (self.objs[0] - object.center[0])**2 + (self.objs[1]- object.center[1])**2 )**0.5  <= self.size + object.radius or self.objs[0] < 10 or self.objs[0] > 1270 or self.objs[1] < 10 or self.objs[1] > 710:
                return "FAILURE"    
        if goal != None:
            if ( (self.objs[0] - goal.center[0])**2 + (self.objs[1] - goal.center[1])**2 )**0.5  <= self.size + goal.radius :
                return "SUCCESS" 
    
    def em_orbita(self,object): # Identifica se o personagem está em órbita e que tipo de órbita é.
        if ( (self.objs[0] - object.center[0])**2 + (self.objs[1]- object.center[1])**2 )**0.5  <= (object.radius)*object.k/250:
            return object.gravitational_force(self.objs)
        elif ( (self.objs[0] - object.center[0])**2 + (self.objs[1]- object.center[1])**2 )**0.5  <= (object.radius)*object.k/25 :
            return object.gravitational_force(self.objs)/2
        else:
            return 0

    def death(self,stage):
        self.vel = np.array([0,0])
        self.objs = stage.spawn


class Stage():
    def __init__(self, planetas,spawn):
        self.planetas = planetas
        self.spawn = spawn

# Classe dos planetas


class MassCenter():
    def __init__(self,center,radius,image,screen):
        self.center = center
        self.color = image
        self.radius = radius 
        self.screen = screen
        if radius < 25:
            self.k = 2000*radius
        self.k = 1000*radius

    def draw(self):
        pygame.draw.circle(surface = self.screen, radius =self.radius,center=self.center,color=self.color)

    def gravitational_force(self,pos): # Calcula a aceleração Gravitacinal.

        dp = self.center - pos
        d = np.linalg.norm(dp)
        a = (dp/d)*self.k/d**2

        return a
    

class Goal():
    def __init__(self,objs,size,screen):
        self.center = objs
        self.radius = size
        self.color = "yellow"
        self.screen = screen
    
    def draw(self):
        pygame.draw.circle(surface = self.screen, radius = self.radius, center = self.center, color=self.color)