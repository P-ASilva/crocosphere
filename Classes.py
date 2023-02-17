import numpy as np
import pygame 


class CrocoBoy():
    def __init__(self):
        self.color = (30, 200, 20)
        self.vel = np.array([0,0])
        self.objs = np.array([0,0])
        self.size = 5
    
    def rect(self):
        return pygame.Rect(self.objs, (10, 10))
    
    def collide(self,objects,goal=None):
        for object in objects:
            if (self.objs[0]**2 - object.center[0]**2 + self.objs[1]**2 - object.center[1]**2)**0.5  <= self.size + object.radius :
                return "FAILURE"

    def death(self,stage):
        self.vel = np.array([0,0])
        self.objs = stage.spawn

class Stage():
    def __init__(self, planetas,spawn):
        self.planetas = planetas
        self.spawn = spawn
        
class MassCenter():
    planetas = []
    def __init__(self,center,radius,image,screen,k):
        self.center = center
        self.color = image
        self.radius = radius 
        self.screen = screen
        self.k = k

    def draw(self):
        pygame.draw.circle(surface = self.screen, radius =self.radius,center=self.center,color=self.color)

    def gravitational_force(self,pos):

        dp = self.center - pos
        d = np.linalg.norm(dp) # modulo1
        a = (dp/d)*self.k/d**2

        return a

    """
    def planetas(self):
        return planetas
    """



class Goal():
    def __init__(self,x,y,size):
        self.objs = np.array([x,y])
        self.size = size