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
screen = pygame.display.set_mode((1600,950))
#pygame.display.set_mode((0, 0), pygame.FULLSCREEN)




#charger images arriere plan
background=pygame.image.load('assets/bg2.png').convert()
bgOver=pygame.image.load('assets/bg1.png').convert_alpha()
maison=pygame.image.load('assets/bg3.png').convert_alpha()



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

font=pygame.font.Font(None, 50)

#PV Joueur
PV = 1
StrPV = font.render("PV : "+str(PV),1,(16,16,22))

#Score Joueur
score = 0


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


#############################################
#MENU
x=0
y=0
Menu = True
options = False
bouton_down = False
NiveauVolume = 1
NiveauDifficulté = 0
menu_bg =pygame.image.load('assets/bg_menu.png').convert_alpha()

#JOUER
bouton_jouer =pygame.image.load('assets/bouton_jouer_off.png').convert_alpha()
bouton_jouer_rect = bouton_jouer.get_rect()
bouton_jouer_rect.x = 400
bouton_jouer_rect.y = 300

#OPTIONS
bouton_options =pygame.image.load('assets/bouton_options_off.png').convert_alpha()
bouton_options_rect = bouton_options.get_rect()
bouton_options_rect.x = 380
bouton_options_rect.y = 450

#QUITTER
bouton_quitter=pygame.image.load('assets/bouton_quitter_off.png').convert_alpha()
bouton_quitter_rect = bouton_quitter.get_rect()
bouton_quitter_rect.x = 820
bouton_quitter_rect.y = 450

#RETRY
bouton_rejouer=pygame.image.load('assets/bouton_rejouer_off.png').convert_alpha()
bouton_rejouer_rect = bouton_rejouer.get_rect()
bouton_rejouer_rect.x = 380
bouton_rejouer_rect.y = 600

#VOLUME
bouton_volume=pygame.image.load('assets/bouton_volume_10.png').convert_alpha()
bouton_volume_rect = bouton_volume.get_rect()
bouton_volume_rect.x = 380
bouton_volume_rect.y = 450

#VOLUME PLUS
bouton_volume_plus=pygame.image.load('assets/bouton_plus_off.png').convert_alpha()
bouton_volume_plus_rect = bouton_volume_plus.get_rect()
bouton_volume_plus_rect.x = 767
bouton_volume_plus_rect.y = 468

#VOLUME MOINS
bouton_volume_moins=pygame.image.load('assets/bouton_moins_off.png').convert_alpha()
bouton_volume_moins_rect = bouton_volume_moins.get_rect()
bouton_volume_moins_rect.x = 385
bouton_volume_moins_rect.y = 468

#DIFFICULTE
bouton_difficulté=pygame.image.load('assets/bouton_difficulté_0.png').convert_alpha()
bouton_difficulté_rect = bouton_difficulté.get_rect()
bouton_difficulté_rect.x = 820
bouton_difficulté_rect.y = 450

#VOLUME PLUS
bouton_difficulté_plus=pygame.image.load('assets/bouton_plus_off.png').convert_alpha()
bouton_difficulté_plus_rect = bouton_difficulté_plus.get_rect()
bouton_difficulté_plus_rect.x = 1207
bouton_difficulté_plus_rect.y = 468

#VOLUME MOINS
bouton_difficulté_moins=pygame.image.load('assets/bouton_moins_off.png').convert_alpha()
bouton_difficulté_moins_rect = bouton_difficulté_moins.get_rect()
bouton_difficulté_moins_rect.x = 825
bouton_difficulté_moins_rect.y = 468

#RETOUR
bouton_retour =pygame.image.load('assets/bouton_retour_off.png').convert_alpha()
bouton_retour_rect=bouton_retour.get_rect()
bouton_retour_rect.x = 400
bouton_retour_rect.y = 300

#Boucle fenetre, ( donc running = True)
while running:




############################################################################################
                                        #MENU
############################################################################################




    if Menu == True :
        pygame.display.flip()

        # background
        screen.blit(background, (0, 0))
        screen.blit(menu_bg, (0, 0))

        if options == False:

            screen.blit(bouton_jouer, bouton_jouer_rect)
            screen.blit(bouton_options, bouton_options_rect)
            screen.blit(bouton_quitter, bouton_quitter_rect)

        elif options == True:
            #volume
            screen.blit(bouton_volume, bouton_volume_rect)
            screen.blit(bouton_volume_plus, bouton_volume_plus_rect)
            screen.blit(bouton_volume_moins, bouton_volume_moins_rect)

            #difficulté
            screen.blit(bouton_difficulté, bouton_difficulté_rect)
            screen.blit(bouton_difficulté_plus, bouton_difficulté_plus_rect)
            screen.blit(bouton_difficulté_moins, bouton_difficulté_moins_rect)

            screen.blit(bouton_retour, bouton_retour_rect)



        ## Si le focus est sur la fenêtre.
        if pygame.mouse.get_focused():
            ## Trouve position de la souris
            x, y = pygame.mouse.get_pos()

################## BOUTONS #############################












        if options == False:

            #########################               BOUTON QUITTER
            if bouton_quitter_rect.collidepoint(x, y):
                bouton_quitter = pygame.image.load('assets/bouton_quitter_on.png').convert_alpha()
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    # alors runnig = False
                    running = False
                    # et la fenetre se ferme.
                    pygame.quit()
            elif not bouton_quitter_rect.collidepoint(x, y):
                bouton_quitter = pygame.image.load('assets/bouton_quitter_off.png').convert_alpha()

            #######################             BOUTON JOUER
            if bouton_jouer_rect.collidepoint(x, y):
                bouton_jouer = pygame.image.load('assets/bouton_jouer_on.png').convert_alpha()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and bouton_down == False:
                    bouton_down = True
                    # ALORS ON JOUE
                    Menu = False
            elif not bouton_jouer_rect.collidepoint(x, y):
                bouton_jouer = pygame.image.load('assets/bouton_jouer_off.png').convert_alpha()

            #########################               BOUTON OPTIONS
            if bouton_options_rect.collidepoint(x, y):
                bouton_options = pygame.image.load('assets/bouton_options_on.png').convert_alpha()
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    # ALORS ON ACCEDE AUX OPTIONS
                    options = True
            elif not bouton_options_rect.collidepoint(x, y):
                bouton_options = pygame.image.load('assets/bouton_options_off.png').convert_alpha()



        else:

             #########################               BOUTON VOLUME PLUS
            if bouton_volume_plus_rect.collidepoint(x, y):
                bouton_volume_plus = pygame.image.load('assets/bouton_plus_on.png').convert_alpha()
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if NiveauVolume < 1 and bouton_down == False:
                        bouton_down = True
                        NiveauVolume += 0.1
                    bouton_volume = pygame.image.load('assets/bouton_volume_'+str(int(NiveauVolume*10))+'.png').convert_alpha()
                        #Augmenter Volume aussi
            elif not bouton_volume_plus_rect.collidepoint(x, y):
                bouton_volume_plus = pygame.image.load('assets/bouton_plus_off.png').convert_alpha()

            #########################               BOUTON VOLUME MOINS
            if bouton_volume_moins_rect.collidepoint(x, y):
                bouton_volume_moins = pygame.image.load('assets/bouton_moins_on.png').convert_alpha()
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if NiveauVolume > 0 and bouton_down == False:
                        bouton_down = True
                        NiveauVolume -= 0.1
                    bouton_volume = pygame.image.load('assets/bouton_volume_'+str(int(NiveauVolume*10))+'.png').convert_alpha()
                # réduire Volume aussi
            elif not bouton_volume_moins_rect.collidepoint(x, y):
                bouton_volume_moins = pygame.image.load('assets/bouton_moins_off.png').convert_alpha()








            #########################               BOUTON DIFFICULTE PLUS
            if bouton_difficulté_plus_rect.collidepoint(x, y):
                bouton_difficulté_plus = pygame.image.load('assets/bouton_plus_on.png').convert_alpha()
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if NiveauDifficulté < 3 and bouton_down == False:
                        bouton_down = True
                        NiveauDifficulté += 1
                        print(NiveauDifficulté)
                    bouton_difficulté = pygame.image.load('assets/bouton_difficulté_'+str(int(NiveauDifficulté))+'.png').convert_alpha()
                # REDUIRE DIFFICLUTE
            elif not bouton_volume_moins_rect.collidepoint(x, y):
                bouton_difficulté_plus = pygame.image.load('assets/bouton_plus_off.png').convert_alpha()



            #########################               BOUTON DIFFICULTE MOINS
            if bouton_difficulté_moins_rect.collidepoint(x, y):
                bouton_difficulté_moins = pygame.image.load('assets/bouton_moins_on.png').convert_alpha()
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if NiveauDifficulté > 0 and bouton_down == False:
                        bouton_down = True
                        NiveauDifficulté -= 1
                    bouton_difficulté = pygame.image.load('assets/bouton_difficulté_'+str(int(NiveauDifficulté))+'.png').convert_alpha()
                        # REDUIRE DIFFICLUTE
            elif not bouton_volume_moins_rect.collidepoint(x, y):
                bouton_difficulté_moins = pygame.image.load('assets/bouton_moins_off.png').convert_alpha()


            #########################               BOUTON RETOUR MENU
            if bouton_retour_rect.collidepoint(x,y):
                bouton_retour =  pygame.image.load('assets/bouton_retour_on.png').convert_alpha()
                if event.type == MOUSEBUTTONDOWN and bouton_down == False:
                    bouton_down = True
                    options = False
            elif not bouton_retour_rect.collidepoint(x,y):
                bouton_retour = pygame.image.load('assets/bouton_retour_off.png').convert_alpha()



        # Quitter la fenetre
        for event in pygame.event.get():
            # Si on appuie sur la croix pour quitter
            if event.type == pygame.QUIT:
                # alors runnig = False
                running = False
                # et la fenetre se ferme.
                pygame.quit()


        #Permet de cliquer 1 par 1 (pour le volume)
        if event.type == MOUSEBUTTONUP and event.button == 1:
            bouton_down = False

        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            print(event.pos[1])
            print(event.pos[0])


############################################################################################
                                        #JEU
############################################################################################





    if PV != 0 and Menu == False :
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


        #texte

        StrScore = font.render("Score : "+str(score),1,(16,16,22))
        StrPV = font.render("PV : " + str(PV), 1, (16, 16, 22))

        screen.blit(StrScore, (10, 2))
        screen.blit(StrPV, (10, 30))

        screen.blit(StrEffects, (700, 2))


        #Boost vitesse
        Compteur +=1
        if Compteur >= 3000:
            if Compteur == 3000 :
                effet = randint(1,3)


            #vitesse
            if effet == 1 or effet ==2:


                if Boost == False :
                    if effet == 1:
                        game.effects.boost_vitesse()
                        screen.blit(effects.im_vitesse, game.effects.rect_vitesse)
                    elif effet == 2:
                        game.effects.jump_boost()
                        screen.blit(effects.im_jump, game.effects.rect_jump)


                #Si on chope pas le boost
                if Compteur >= 3800 and Boost == False:
                    Compteur =0
                    Boost = False

                #Si on chope le boost :
                if effet == 1:
                    if game.player.joueur.colliderect(game.effects.rect_vitesse):
                        StrEffects = font.render("Speed Boost !",1,(0,90,63))
                        Boost = True

                elif effet == 2:
                    if game.player.joueur.colliderect(game.effects.rect_jump):
                        Boost = True
                        game.player.Jump_Boost = True
                        StrEffects = font.render("Jump Boost !", 1, (177, 0, 250))


                if Boost == True:
                    if effet == 1:
                        if compteur_temps_boost == 0:
                            game.effects.rect_vitesse.x = randint(200,1400)
                            game.effects.y_i= randint(100,580)
                        game.player.vitesse = 5

                    elif effet == 2:
                        if compteur_temps_boost == 0:
                            game.effects.rect_jump.x = randint(200, 1400)
                            game.effects.y_j = randint(100, 580)

                    compteur_temps_boost += 1

                if compteur_temps_boost >= 2000:
                    compteur_temps_boost = 0
                    Compteur =0
                    Boost = False
                    StrEffects = font.render("", 1, (16, 16, 22))
                    if effet ==1:
                        game.player.vitesse = 3
                    elif effet == 2:
                        game.player.Jump_Boost = False
                        game.player.saut = 0








            #mystere
            if effet == 3:
                if Boost == False :
                    game.effects.random_effect()
                    screen.blit(effects.im_mystere, game.effects.rect_mystere)

                #Si on chope pas le boost
                if Compteur >= 3800 and Boost == False:
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
                        game.gravite = 1
                        StrEffects = font.render("Gravité plus faible !", 1, (177, 0, 250))

                    if mystere == 2 :
                        game.gravite = 6
                        StrEffects = font.render("Gravité plus forte !", 1, (165, 0, 15))

                    if mystere == 3:
                        if tmp == 0:
                            tmp = game.enemy.vitesse
                        game.enemy.vitesse = 0.7
                        StrEffects = font.render("Papillon ralenti !", 1, (165, 0, 15))

                    if mystere == 4:
                        game.player.vitesse = 1
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


                    if compteur_temps_boost >= 2000:
                        compteur_temps_boost = 0
                        Compteur =0
                        Boost = False

                        if mystere == 1 or mystere == 2 :
                            game.gravite = 3

                        if mystere == 3:
                            game.enemy.vitesse = tmp

                        if mystere == 4:
                            game.player.vitesse = 3

                        tmp = 0
                        mystere = 0
                        StrEffects = font.render("", 1, (16, 16, 22))


        #Si le papillon quitte la fenetre == il atteint l'objectif

        if game.enemy.enemy.x > -50:
            game.enemy.move()
            #image enemy
            screen.blit(enemy.im_enemy, game.enemy.enemy)
        elif game.enemy.enemy.x <= -50:

            game.enemy.enemy.x = randint(1700,2000)
            PV -= 1
            game.enemy.move()




        #Afficher maison
        screen.blit(maison, (0, 291))



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
        if game.pressed.get(pygame.K_LEFT) and game.player.joueur.x > 120:
            game.player.move_left()


        #descendre plateforme
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and collision_sol == False:
                game.player.joueur.y += 2


        #Permettre double saut au perso
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game.player.double_saut<20:
                game.player.J_saute = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game.player.double_saut>20:
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
                game.resistance = -1
            elif mystere == 2 and Boost == True :
                game.resistance = -6
            else :
                game.resistance = -3
            game.player.double_saut = 0
            if game.sol.sol_principal.colliderect(game.player.joueur):
                collision_sol = True

        else :
            game.resistance= 0
            collision_sol = False





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




############################################################################################
                                        #PERDU
############################################################################################





    if PV == 0 :

        bouton_quitter_rect.x = 820
        bouton_quitter_rect.y = 600


        # mise a jour ecran
        pygame.display.flip()
        # gravité dans le jeu
        game.gravite_jeu()

        # background
        screen.blit(background, (0, 0))
        # plateforme 1
        screen.blit(plateforme.im_plateforme, game.plateforme.plateforme_1)
        # plateforme 2
        screen.blit(plateforme.im_plateforme, game.plateforme.plateforme_2)
        # plateforme 2
        screen.blit(plateforme.im_plateforme, game.plateforme.plateforme_3)
        # image joueur
        screen.blit(player.im_joueur, game.player.joueur)

        # texte

        StrScore = font.render("Score : " + str(score), 1, (16, 16, 22))
        StrPV = font.render("PV : " + str(PV), 1, (16, 16, 22))

        screen.blit(StrScore, (10, 2))
        screen.blit(StrPV, (10, 30))

        screen.blit(StrEffects, (700, 2))


        #ecran game over
        screen.blit(bgOver, (0, 0))
        screen.blit(bouton_quitter, bouton_quitter_rect)
        screen.blit(bouton_rejouer, bouton_rejouer_rect)

        ## Si le focus est sur la fenêtre.
        if pygame.mouse.get_focused():
            ## Trouve position de la souris
            x, y = pygame.mouse.get_pos()

            if bouton_rejouer_rect.collidepoint(x, y):
                bouton_rejouer=pygame.image.load('assets/bouton_rejouer_on.png').convert_alpha()
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    PV = 1
                    score = 0
                    game.player.joueur.x = 400
                    game.player.joueur.y = 0
                    game.enemy.vitesse = 1
                    Compteur = 600
                    game.pressed ={}
                    compteur_temps_boost = 0
                    Boost = False
                    game.player.vitesse = 3
                    game.player.Jump_Boost = False
                    game.gravite = 3
                    game.resistance = 0
                    tmp = 0
                    mystere = 0
                    StrEffects = font.render("", 1, (16, 16, 22))

            elif not bouton_rejouer_rect.collidepoint(x, y):
                bouton_rejouer=pygame.image.load('assets/bouton_rejouer_off.png').convert_alpha()

            if bouton_quitter_rect.collidepoint(x, y):
                bouton_quitter = pygame.image.load('assets/bouton_quitter_on.png').convert_alpha()
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    # alors runnig = False
                    running = False
                    # et la fenetre se ferme.
                    pygame.quit()
            elif not bouton_quitter_rect.collidepoint(x, y):
                bouton_quitter = pygame.image.load('assets/bouton_quitter_off.png').convert_alpha()

        # Quitter la fenetre
        for event in pygame.event.get():
            # Si on appuie sur la croix pour quitter
            if event.type == pygame.QUIT:
                # alors runnig = False
                running = False
                # et la fenetre se ferme.
                pygame.quit()


