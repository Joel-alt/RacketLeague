import pygame
from math import sin


#class enemy
class Enemy(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        
        #coords+image enemy
        self.im_enemy = pygame.image.load('assets/enemy.png').convert_alpha()
        self.enemy = self.im_enemy.get_rect()
        self.enemy.x=2200
        self.enemy.y=500
        self.y_e = 500
        
        self.vitesse= 1
        self.i=0
        self.amplitude=25
        
        self.compteur = 0


        #enemy 2 :
        self.im_enemy_2= pygame.image.load('assets/enemy_2.png').convert_alpha()
        self.enemy_2_rect = self.im_enemy_2.get_rect()
        self.enemy_2_rect.x = 2000
        self.enemy_2_rect.y = 50


   
   
   
    def move(self):
        self.enemy.x -= self.vitesse
        self.enemy.y = self.y_e + sin(self.i)*self.amplitude
        self.compteur += 1
        
        
        if self.i>=0 and self.i!= 180 : 
            self.i += 0.03
            self.compteur = 0
        
        elif self.i== 180:
            self.i=0

    # la fonction sinus va trop vite, du coup le papillon s'affiche mal, donc je fais un compteur pour faire varier la valeur de i plus lentement .
    #edit, j'ai remplacé self.i += 1 par += 0.1, et c'est beaucoup mieux !

    """def move_2(self):
        self.enemy_2_rect.x -=  self.vitesse
        
        if self.enemy_2_rect.y == 200:
            self.enemy_2_rect.y += 2
            
        
        elif self.hauteur :
            self.enemy_2_rect.y -= 2
        """


