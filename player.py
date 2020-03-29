import pygame

#class joueur
class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        
        #coords+image joueur
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x=400
        self.rect.y=000
        
        #carac joueur
        self.vitesse = 7
        
        #saut
        self.J_saute = False
        self.saut = 35
        
        
        
    def move_right(self):
        self.rect.x += self.vitesse
    
    def move_left(self):
        self.rect.x -= self.vitesse
        
    def sauter(self):
        
        if self.J_saute == True :

            if self.saut <= 0:
                self.saut = 35
                self.J_saute  = False
                
            else :
                self.saut = self.saut -1
                print(self.saut)
                
        
        self.rect.y = self.rect.y - (self.saut)