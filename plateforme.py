import pygame


class Plateforme(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.im_plateforme = pygame.image.load('assets/plateforme.png')
        self.plateforme_1 = self.im_plateforme.get_rect()
        self.plateforme_1.x = 100
        self.plateforme_1.y = 400

        self.plateforme_2 = self.im_plateforme.get_rect()
        self.plateforme_2.x = 1000
        self.plateforme_2.y = 450

        self.plateforme_3 = self.im_plateforme.get_rect()
        self.plateforme_3.x = 600
        self.plateforme_3.y = 200