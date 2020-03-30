import pygame

#class joueur
class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        
        #coords+image joueur
        self.image = pygame.image.load('assets/player.png')
        self.image_2 = pygame.image.load('assets/player_2.png')
        self.rect = self.image.get_rect()
        self.rect.x=400
        self.rect.y=000
        
        #carac joueur
        self.vitesse = 7
        
        #saut
        self.J_saute = False
        self.Jump_Boost = False
        self.saut = 30
        self.double_saut = 0
        
        
        
        
    def move_right(self):
        self.rect.x += self.vitesse
        self.image = pygame.image.load('assets/player.png')
    
    def move_left(self):
        self.rect.x -= self.vitesse
        self.image = pygame.image.load('assets/player_2.png')
        
    def sauter(self):
        
        if self.J_saute == True:
            
            if self.Jump_Boost == False :
                
                if self.saut <= 0:
                    self.saut = 30
                    self.double_saut += 30
                    self.J_saute  = False
                    
                else :
                    self.saut = self.saut -1
                    self.rect.y = self.rect.y - (self.saut)
                
            elif self.Jump_Boost == True :
   
                if self.saut <= 0:
                    self.saut = 35
                    self.double_saut += 35
                    self.J_saute  = False
                    
                else :
                    self.saut = self.saut -1
                    self.rect.y = self.rect.y - (self.saut)
   
    
        