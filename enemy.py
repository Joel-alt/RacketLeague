import pygame
from math import sin


#class enemy
class Enemy(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        
        #coords+image enemy
        self.image = pygame.image.load('assets/enemy.png')
        self.rect = self.image.get_rect()
        self.rect.x=1200
        self.rect.y=200
        
        self.vitesse=4
        self.i=0
        
        self.compteur = 0
   
   
   
    def move(self):
        self.rect.x -= self.vitesse
        self.rect.y = 200 + sin(self.i)*25
        self.compteur += 1
        
        
        if self.i>=0 and self.i!= 180 : 
            self.i += 0.1
            self.compteur = 0
        
        elif self.i== 180:
            self.i=0


    # la fonction sinus va trop vite, du coup le papillon s'affiche mal, donc jefais un compteur pour faire varier la valeur de i plus lentement .
    #edit, j'ai remplacé self.i += 1 par += 0.1, et c'est beaucoup mieux !