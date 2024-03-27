#pour menu
import pygame

class menu():
    def __init__(self):
        self.button_start = pygame.image.load('Asset/Menu/button_start.png')
        self.button_start = pygame.transform.scale(self.button_start,(210,200))
        self.rect_start = self.button_start.get_rect()
        self.rect_start.topleft = (300,150)

        self.button_setting = pygame.image.load('Asset/Menu/button_setting.png')
        self.button_setting = pygame.transform.scale(self.button_setting,(210,190))
        self.rect_setting = self.button_setting.get_rect()
        self.rect_setting.topleft = (300,300)

        self.button_exit = pygame.image.load('Asset/Menu/button_exit.png')
        self.button_exit = pygame.transform.scale(self.button_exit,(200,200))
        self.rect_exit = self.button_exit.get_rect()
        self.rect_exit.topleft = (300,450)






'''
# creation du bouton cliquable
if event.type == pygame.MOUSEBUTTONDOWN:
    if button_rect.collidepoint(event.pos):
        game.is_playing = True
    # si le bouton de jeux est selectioné le jeux change d'etat et ce lance
'''