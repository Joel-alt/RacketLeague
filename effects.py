import pygame
from math import sin
from random import *
#class effets
class Effects(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        
        #Boost vitesse
        self.im_vitesse = pygame.image.load('assets/vitesse.png')
        self.compteur = 0
        self.rect_vitesse = self.im_vitesse.get_rect()
        self.rect_vitesse.y = 440
        #permet d'utiliser /random et conserver la valeur, voir main
        self.y_i = 440
        self.rect_vitesse.x = 800
        self.i=0
        
        
        
        #Jump Boost
        self.im_jump = pygame.image.load('assets/jump_boost.png')
        self.rect_jump = self.im_jump.get_rect()
        self.rect_jump.y = 440
        #permet d'utiliser /random et conserver la valeur, voir main
        self.y_j = 440
        self.rect_jump.x = 300
        
        
        
        
         #random effect
        self.im_mystere = pygame.image.load('assets/random_effect.png')
        self.rect_mystere = self.im_mystere.get_rect()
        self.rect_mystere.y = 440
        #permet d'utiliser /random et conserver la valeur, voir main
        self.y_m = 440
        self.rect_mystere.x = 300
        
        
    def boost_vitesse(self):
        self.rect_vitesse.y = self.y_i + sin(self.i)*10
        
        
        self.compteur += 1
        if self.i>=0 and self.i!= 180 : 
            self.i += 0.1
            self.compteur = 0
        
        elif self.i== 180:
            self.i=0
    
    
    def jump_boost(self):
        self.rect_jump.y = self.y_j + sin(self.i)*10


        self.compteur += 1
        if self.i>=0 and self.i!= 180 : 
            self.i += 0.1
            self.compteur = 0
        
        elif self.i== 180:
            self.i=0
            
            
    def random_effect(self):
        self.rect_mystere.y = self.y_m + sin(self.i)*10


        self.compteur += 1
        if self.i>=0 and self.i!= 180 : 
            self.i += 0.1
            self.compteur = 0
        
        elif self.i== 180:
            self.i=0