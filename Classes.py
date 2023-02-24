import numpy as np
import pygame 


class CrocoBoy():
    def __init__(self):
        self.color = (30, 200, 20)
        self.vel = np.array([0,0])
        self.objs = np.array([0,0])
        self.size = 12
    
    def rect(self):
        return pygame.Rect(self.objs, (self.size, self.size))
    
    def collide(self,objects,goal=None): # Verifica se houve colisão com o objetivo,planeta ou fim da tela.
        for object in objects:
            if ( (self.objs[0] - object.center[0])**2 + (self.objs[1]- object.center[1])**2 )**0.5  <= self.size + object.radius or self.objs[0] < 10 or self.objs[0] > 1270 or self.objs[1] < 10 or self.objs[1] > 710:
                return "FAILURE"    
        if goal != None:
            if ( (self.objs[0] - goal.center[0])**2 + (self.objs[1] - goal.center[1])**2 )**0.5  <= self.size + goal.radius :
                return "SUCCESS"
    
    
    def em_orbita(self,object):
        if ( (self.objs[0] - object.center[0])**2 + (self.objs[1]- object.center[1])**2 )**0.5  <= (object.radius)*4 :
            return object.gravitational_force(self.objs)
        else:
            return 0


    def death(self,stage):
        self.vel = np.array([0,0])
        self.objs = stage.spawn


class Stage():
    def __init__(self, planetas,spawn):
        self.planetas = planetas
        self.spawn = spawn


class MassCenter():
    def __init__(self,center,radius,image,screen):
        self.center = center
        self.color = image
        self.radius = radius 
        self.screen = screen
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