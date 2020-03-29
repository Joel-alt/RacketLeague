import pygame

class Sol(pygame.sprite.Sprite):
    
    def __init__(self):
        
        super().__init__()
        self.sol_principal = pygame.Rect(0,500,1600,1600)
