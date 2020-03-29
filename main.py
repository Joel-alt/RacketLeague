import pygame

from game import Game
from player import Player
from sol import Sol

pygame.init()

# Titre fenetre
pygame.display.set_caption("VR7")
# Taille fenetre
screen = pygame.display.set_mode((1200, 800))
# charger image arriere plan
background = pygame.image.load('assets/bg1.jpg')
# chargement classe Player(), etc...
player = Player()
# chargement jeu
game = Game()
# variable qui reste vraie tant que la fenetre est ouverte
running = True
# Variable collision sol
collision_sol = False

# Boucle fenetre, ( donc running = True)
while running:

    # mise a jour ecran
    pygame.display.flip()
    # p=gravité dans le jeu
    game.gravite_jeu()
    # background
    screen.blit(background, (0, 0))
    # joueur
    screen.blit(player.image, game.player.rect)

    # si le perso touche le sol, alors il arrete de tomber.
    if game.sol.sol_principal.colliderect(game.player.rect):
        game.resistance = -7
        collision_sol = True

    else:
        game.resistance = 0

    for event in pygame.event.get():
        # Si on appuie sur la croix pour quitter
        if event.type == pygame.QUIT:
            # alors runnig = False
            running = False
            # et la fenetre se ferme.
            pygame.quit()

    if event.type == pygame.KEYDOWN:
        game.pressed[event.key] = True
    if event.type == pygame.KEYUP:
        game.pressed[event.key] = False

    # Déplacements à droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x < 1550:
        # fonction créée dans la class player
        game.player.move_right()
    # Déplacement à gauche
    if game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()
    if game.pressed.get(pygame.K_UP) and game.player.J_saute == False:
        game.player.J_saute = True

    if game.player.J_saute == True and collision_sol:
        game.player.sauter()
        print(game.player.J_saute)
