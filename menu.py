#pour menu
import pygame

class menu():
    def __init__(self):
        self.button_start = pygame.image.load('Asset/Menu/button_start.png')
        self.rect_start = self.button_start.get_rect()

        self.button_setting = pygame.image.load('Asset/Menu/button_setting.png')
        self.rect_setting = self.button_setting.get_rect()

        self.button_exit = pygame.image.load('Asset/Menu/button_exit.png')
        self.rect_exit = self.button_exit.get_rect()






# creation du bouton cliquable
if event.type == pygame.MOUSEBUTTONDOWN:
    if button_rect.collidepoint(event.pos):
        game.is_playing = True
    # si le bouton de jeux est selectioné le jeux change d'etat et ce lance