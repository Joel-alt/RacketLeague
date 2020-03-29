import pygame
from player import Player
from sol import Sol


#class jeu
class Game:

    def __init__(self):
        #génération joueur
        self.player = Player()
        self.pressed = {}  # touches actionnées par le joueur
        self.sol = Sol()
        self.gravite = 7
        self.resistance = 0
        
    def gravite_jeu(self):
        self.player.rect.y += self.gravite + self.resistance