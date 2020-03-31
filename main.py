import pygame
from pygame.locals import *
from random import *

from game import Game
from player import Player
from sol import Sol
from enemy import Enemy
from effects import Effects
from plateforme import Plateforme

pygame.init()


#Titre fenetre
pygame.display.set_caption("VR7")
#Taille fenetre
screen = pygame.display.set_mode((1600,800))




#charger image arriere plan
background=pygame.image.load('assets/bg2.png').convert()




#chargement classe Player(), etc...
player = Player()
#chargement jeu
game = Game()
#chargement sol
sol = Sol()
#Plateforme
plateforme = Plateforme()
#chargement enemy
enemy = Enemy()
#chargement effets
effects = Effects()




#Score Joueur
score = 0
font=pygame.font.Font(None, 50)
#Texte score
StrScore = font.render("Score : "+str(score),1,(16,16,22))
#text effets
StrEffects = font.render("",1,(16,16,22))

#variable qui reste vraie tant que la fenetre est ouverte
running=True
#Variable collision sol
collision_sol = False

#compteur apparition vitesse
Compteur = 600
#Boost vitesse off de base
Boost= False
compteur_temps_boost = 0
effet=0
mystere = 0
tmp = 0



#Boucle fenetre, ( donc running = True)
while running:
    
    #mise a jour ecran
    pygame.display.flip()
    #gravité dans le jeu
    game.gravite_jeu()
    
    
    #background
    screen.blit(background, (0, 0))
    #plateforme 1
    screen.blit(plateforme.im_plateforme, game.plateforme.plateforme_1)
    #plateforme 2
    screen.blit(plateforme.im_plateforme, game.plateforme.plateforme_2)
    # plateforme 2
    screen.blit(plateforme.im_plateforme, game.plateforme.plateforme_3)
    #image joueur
    screen.blit(player.im_joueur, game.player.joueur)
    
    
    
    

    StrScore = font.render("Score : "+str(score),1,(16,16,22))
    #texte
    screen.blit(StrScore, (10, 2))
    screen.blit(StrEffects, (700, 2))
    
    
    #Boost vitesse
    Compteur +=1
    if Compteur >= 800:
        if Compteur == 800 :
            effet = randint(1,3)
        
        
        #vitesse
        if effet == 1:
            if Boost == False :
                game.effects.boost_vitesse()
                screen.blit(effects.im_vitesse, game.effects.rect_vitesse)
            
            #Si on chope pas le boost
            if Compteur >= 1000 and Boost == False:
                Compteur =0
                Boost = False
        
            #Si on chope le boost :
            if game.player.joueur.colliderect(game.effects.rect_vitesse):
                Boost = True
                StrEffects = font.render("Speed Boost !",1,(0,90,63))
                
            if Boost == True:
                if compteur_temps_boost == 0:
                    game.effects.rect_vitesse.x = randint(200,1400)
                    game.effects.y_i= randint(100,580)
                compteur_temps_boost +=1
                game.player.vitesse = 12
                
            if compteur_temps_boost >= 500:
                compteur_temps_boost = 0
                Compteur =0
                Boost = False
                game.player.vitesse = 7
                StrEffects = font.render("",1,(16,16,22))
                
            
        
        
        #jump    
        if effet == 2:
            if Boost == False :
                game.effects.jump_boost()
                screen.blit(effects.im_jump, game.effects.rect_jump)
            
            #Si on chope pas le boost
            if Compteur >= 1000 and Boost == False:
                Compteur =0
                Boost = False
        
            #Si on chope le boost :
            if game.player.joueur.colliderect(game.effects.rect_jump):
                Boost = True
                game.player.Jump_Boost = True
                StrEffects = font.render("Jump Boost !", 1, (177, 0, 250))
                
            if Boost == True:
                if compteur_temps_boost == 0:
                    game.effects.rect_jump.x = randint(200,1400)
                    game.effects.y_j= randint(100,580)
                compteur_temps_boost +=1
                
                if compteur_temps_boost >= 500:
                    compteur_temps_boost = 0
                    Compteur =0
                    Boost = False
                    game.player.Jump_Boost = False
                    game.player.saut= 30
                    StrEffects = font.render("", 1, (16, 16, 22))

        
        #mystere
        if effet == 3:
            if Boost == False :
                game.effects.random_effect()
                screen.blit(effects.im_mystere, game.effects.rect_mystere)
            
            #Si on chope pas le boost
            if Compteur >= 1000 and Boost == False:
                Compteur =0
                Boost = False
        
            #Si on chope le boost :
            if game.player.joueur.colliderect(game.effects.rect_mystere):
                Boost = True
                
            if Boost == True:
                if compteur_temps_boost == 0:
                    game.effects.rect_mystere.x = randint(200,1400)
                    game.effects.y_m= randint(100,580)
                    mystere = randint(1,6)
                compteur_temps_boost +=1
                
                #1 gravité plus faible
                #2 gravité plus forte
                #3 papillon plus lent
                #4 saute moins haut
                #5 perso plus lent
                #6 +5 sur le score
                #7 -3 score
                #8 +3 PV
                #9 -2 PV
                
                
                

                if mystere == 1 :
                    game.gravite = 3
                    StrEffects = font.render("Gravité plus faible !", 1, (177, 0, 250))
                
                if mystere == 2 :
                    game.gravite = 16
                    StrEffects = font.render("Gravité plus forte !", 1, (165, 0, 15))

                if mystere == 3:
                    if tmp == 0:
                        tmp = game.enemy.vitesse
                    game.enemy.vitesse = 4
                    StrEffects = font.render("Papillon ralenti !", 1, (165, 0, 15))

                if mystere == 4:
                    game.player.vitesse = 3
                    StrEffects = font.render("Vitesse ralentie !", 1, (165, 0, 15))

                if mystere == 5:
                    if tmp == 0 :
                        tmp = randint(1,5)
                        score += tmp
                    StrEffects = font.render("Bonus : + "+str(tmp)+"points !", 1, (165, 0, 15))

                if mystere == 6:
                    if tmp == 0 :
                        tmp = randint(1,5)
                        score -= tmp
                    StrEffects = font.render("Malus : - "+str(tmp)+"points !", 1, (165, 0, 15))


                if compteur_temps_boost >= 500:
                    compteur_temps_boost = 0
                    Compteur =0
                    Boost = False
                    
                    if mystere == 1 or mystere == 2 :
                        game.gravite = 9

                    if mystere == 3:
                        game.enemy.vitesse = tmp

                    if mystere == 4:
                        game.player.vitesse = 7

                    tmp = 0
                    mystere = 0
                    StrEffects = font.render("", 1, (16, 16, 22))
    
    
    #Si le papillon quitte la fenetre == il atteint l'objectif
            
    if game.enemy.enemy.x > -50:
        game.enemy.move()
        #image enemy
        screen.blit(enemy.im_enemy, game.enemy.enemy)
    elif game.enemy.enemy.x <= -50:

        game.enemy.enemy.x = 1700
        game.enemy.move()

    
    
    
    
    #Quitter la fenetre
    for event in pygame.event.get():
        #Si on appuie sur la croix pour quitter
        if event.type == pygame.QUIT:
            #alors runnig = False
            running= False
            #et la fenetre se ferme.
            pygame.quit()                  
            
    
    
    
    
    
    #Déplacements à droite

    #Déplacement à droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.joueur.x <1550:
        #fonction créée dans la class player
        game.player.move_right()
        
        
    #Déplacement à gauche
    if game.pressed.get(pygame.K_LEFT) and game.player.joueur.x > 0:
        game.player.move_left()


    #descendre plateforme
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN and game.plateforme.plateforme_1.colliderect(game.player.joueur) \
            or event.key == pygame.K_DOWN and game.plateforme.plateforme_2.colliderect(game.player.joueur) \
            or event.key == pygame.K_DOWN and game.plateforme.plateforme_3.colliderect(game.player.joueur) :
            game.player.joueur.y += 2

        
    #Permettre double saut au perso
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP and game.player.double_saut<60:
            game.player.J_saute = True
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP and game.player.double_saut>60:
            game.player.J_saute = False
        
    if game.player.J_saute==True:
        game.player.sauter()
        
        
    #Pour initialiser pressed
    if event.type == pygame.KEYDOWN:
        game.pressed[event.key] = True
    if event.type == pygame.KEYUP:    
        game.pressed[event.key] = False



    #si le perso touche le sol, alors il arrete de tomber.
    if game.sol.sol_principal.colliderect(game.player.joueur) or game.player.joueur.midbottom[1] // 10 * 10 == game.plateforme.plateforme_1.top and game.plateforme.plateforme_1.colliderect(game.player.joueur)\
            or game.player.joueur.midbottom[1] // 10 * 10 == game.plateforme.plateforme_2.top and game.plateforme.plateforme_2.colliderect(game.player.joueur)\
            or game.player.joueur.midbottom[1] // 10 * 10 == game.plateforme.plateforme_3.top and game.plateforme.plateforme_3.colliderect(game.player.joueur):

        if mystere == 1 and Boost == True :
            game.resistance = -3
        elif mystere == 2 and Boost == True :
            game.resistance = -16
        else :
            game.resistance = -9
        game.player.double_saut = 0
        collision_sol = True
    
    else :
        game.resistance= 0
     
     
     
     
     
    #Si on attrape un papillon
        
    if game.enemy.enemy.y <= game.player.joueur.midright[1] and game.enemy.enemy.y >= game.player.joueur.topright[1] and game.player.joueur.colliderect(game.enemy.enemy) :
        
        game.enemy.enemy.x = randint(1700, 2200)
        game.enemy.y_e = randint(100,600)
        game.enemy.amplitude = randint(10,150)

        if score == 2 or score == 6 or score == 10:
            game.enemy.vitesse +=1
        if score == 15 or score == 20 or score >= 25:
            game.enemy.vitesse +=2

        score += 1
        game.enemy.move()
    
    if event.type == MOUSEBUTTONDOWN and event.button == 1:
        print(event.pos[1])
        print(event.pos[0])

        
    
