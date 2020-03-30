import pygame
from player import Player
from sol import Sol
from enemy import Enemy


#class jeu
class Game:

    def __init__(self):
        #génération joueur
        self.player = Player()
        #génération enemy
        self.enemy = Enemy()
        #génération sol
        self.sol = Sol()
        
        
        #définir pressed
        self.pressed = {}  #touches actionnées par le joueur
        
        #création gravité
        self.gravite = 7
        self.resistance = 0
        
    def gravite_jeu(self):
        self.player.rect.y += self.gravite + self.resistance