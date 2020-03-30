import pygame

from game import Game
from player import Player
from sol import Sol
from enemy import Enemy

pygame.init()


#Titre fenetre
pygame.display.set_caption("VR7")
#Taille fenetre
screen = pygame.display.set_mode((1600,800))




#charger image arriere plan
background=pygame.image.load('assets/bg1.jpg')




#chargement classe Player(), etc...
player = Player()
#chargement jeu
game = Game()
#chargement sol
sol = Sol()
#chargement enemy
enemy = Enemy()




#variable qui reste vraie tant que la fenetre est ouverte
running=True
#Variable collision sol
collision_sol = False


#Boucle fenetre, ( donc running = True)
while running:
    
    #mise a jour ecran
    pygame.display.flip()
    #p=gravité dans le jeu
    game.gravite_jeu()
    
    
    #background
    screen.blit(background, (0, 0))
    #image joueur
    screen.blit(player.image, game.player.rect)
    #image enemy
    screen.blit(enemy.image, game.enemy.rect)
    
    
    
    #Quitter la fenetre 
    for event in pygame.event.get():
        #Si on appuie sur la croix pour quitter
        if event.type == pygame.QUIT:
            #alors runnig = False
            running= False
            #et la fenetre se ferme.
            pygame.quit()
    
    if game.enemy.rect.x > -50:        
        game.enemy.move()
    elif game.enemy.rect.x <= -50:
        #suppression image papillon --> on blit le bg et le player.

        #background
        screen.blit(background, (0, 0))
        #image joueur
        screen.blit(player.image, game.player.rect)
        game.enemy.rect.x = 1600
        game.enemy.rect.y = 200
        game.enemy.move()

                       
            
    #Déplacements à droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x <1550:
        #fonction créée dans la class player
        game.player.move_right()
    #Déplacement à gauche
    if game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()
        
        
    #Saut
    if game.pressed.get(pygame.K_UP) and game.player.double_saut<50:
        game.player.J_saute = True
    elif game.pressed.get(pygame.K_UP) and game.player.double_saut<50:
        game.player.J_saute = False
        
    if game.player.J_saute==True:
        game.player.sauter()
        
        
        
    if event.type == pygame.KEYDOWN:
        game.pressed[event.key] = True
    if event.type == pygame.KEYUP:    
        game.pressed[event.key] = False
            
    

    #si le perso touche le sol, alors il arrete de tomber.
    if game.sol.sol_principal.colliderect(game.player.rect):
        game.resistance = -7
        game.player.double_saut = 0
        collision_sol = True
    
    else :
        game.resistance= 0
        
    if game.enemy.rect.y <= game.player.rect.midright[1] and game.enemy.rect.y >= game.player.rect.topright[1] and game.player.rect.colliderect(game.enemy.rect):
        #background
        screen.blit(background, (0, 0))
        #image joueur
        screen.blit(player.image, game.player.rect)
        game.enemy.rect.x = 1600
        game.enemy.rect.y = 200
        game.enemy.move()
    
