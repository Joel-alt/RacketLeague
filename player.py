import pygame

#class joueur
class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        
        #coords+image joueur
        self.im_joueur = pygame.image.load('assets/player.png').convert_alpha()
        self.joueur = self.im_joueur.get_rect()
        self.joueur.x=400
        self.joueur.y=000
        
        #carac joueur
        self.vitesse = 3
        
        #saut
        self.J_saute = False
        self.Jump_Boost = False
        self.saut = 10
        self.double_saut = 0
        

        
        
    def move_right(self):
        self.joueur.x += self.vitesse
    
    def move_left(self):
        self.joueur.x -= self.vitesse
        
    def sauter(self):
        
        if self.J_saute == True:
            
            if self.Jump_Boost == False :
                
                if self.saut <= 0:
                    self.saut = 10
                    self.double_saut += 10
                    self.J_saute  = False
                    
                else :
                    self.saut = self.saut -0.1
                    self.joueur.y = self.joueur.y - (self.saut)
                
            elif self.Jump_Boost == True :
   
                if self.saut <= 0:
                    self.saut = 10
                    self.double_saut += 10
                    self.J_saute  = False
                    
                else :
                    self.saut = self.saut -0.06
                    self.joueur.y = self.joueur.y - (self.saut)
   
    
        