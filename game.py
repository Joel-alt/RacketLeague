import pygame
from player import Player
from sol import Sol
from enemy import Enemy
from effects import Effects
from plateforme import Plateforme
from sonore import Sonore


#class jeu
class Game:

    def __init__(self):
        #chargement joueur
        self.player = Player()
        #chargement enemy
        self.enemy = Enemy()
        #chargement sol
        self.sol = Sol()
        #chargement effects
        self.effects = Effects()
        #chargement plateforme
        self.plateforme = Plateforme()
        #chargement sonore
        self.sonore = Sonore()
        
        
        #définir pressed
        self.pressed = {}  #touches actionnées par le joueur
        
        #création gravité
        self.gravite = 3
        self.resistance = 0
        
    def gravite_jeu(self):
        self.player.joueur.y += self.gravite + self.resistance