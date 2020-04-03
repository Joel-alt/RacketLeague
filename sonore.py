import pygame

class Sonore:

    def __init__(self):
        self.music_jeu_normal = pygame.mixer.Sound("sons/music.ogg")
        self.music_jeu_hard = pygame.mixer.Sound("sons/music_hardcore.ogg")
        self.menu_sound = pygame.mixer.Sound("sons/menu_sound.ogg")

        self.game_over_1_sound = pygame.mixer.Sound("sons/mort_1.ogg")
        self.game_over_2_sound = pygame.mixer.Sound("sons/mort_2.ogg")

        self.speed_sound = pygame.mixer.Sound("sons/speed.ogg")
        self.jump_boost_sound = pygame.mixer.Sound("sons/jump_boost.ogg")
        self.random_effects_sound = pygame.mixer.Sound("sons/random_effects.ogg")
        self.lose_PV_sound = pygame.mixer.Sound("sons/lose_PV.ogg")

        self.jump_sound = pygame.mixer.Sound("sons/jump.ogg")
        self.swoosh_sound = pygame.mixer.Sound("sons/swoosh.ogg")

        self.pop_up_sound = pygame.mixer.Sound("sons/pop_up.ogg")
        self.clic_sound = pygame.mixer.Sound("sons/clic.ogg")

        self.NiveauVolume = 1
        self.son_loser = False




    def Volume(self):
        pygame.mixer.music.set_volume(self.NiveauVolume)
        self.music_jeu_normal.set_volume(self.NiveauVolume)
        self.music_jeu_hard.set_volume(self.NiveauVolume)
        self.game_over_1_sound.set_volume(0.5*self.NiveauVolume)
        self.game_over_2_sound.set_volume(0.5*self.NiveauVolume)
        self.speed_sound.set_volume(self.NiveauVolume)
        self.jump_boost_sound.set_volume(self.NiveauVolume)
        self.random_effects_sound.set_volume(self.NiveauVolume)
        self.jump_sound.set_volume(self.NiveauVolume)
        self.swoosh_sound.set_volume(self.NiveauVolume)
        self.menu_sound.set_volume(self.NiveauVolume)
        self.pop_up_sound.set_volume(self.NiveauVolume)
        self.clic_sound.set_volume(self.NiveauVolume)
        self.lose_PV_sound.set_volume(self.NiveauVolume)
