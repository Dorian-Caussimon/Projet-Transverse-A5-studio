#pour menu
import pygame

class menu():
    def __init__(self):
        self.button_start = pygame.image.load('Asset/Menu/button_start.png')
        self.button_start = pygame.transform.scale(self.button_start,(210,200))
        self.rect_start = self.button_start.get_rect()
        self.rect_start.center = (400,200)

        self.button_setting = pygame.image.load('Asset/Menu/button_setting.png')
        self.button_setting = pygame.transform.scale(self.button_setting,(210,190))
        self.rect_setting = self.button_setting.get_rect()
        self.rect_setting.center = (400,350)

        self.button_exit = pygame.image.load('Asset/Menu/button_exit.png')
        self.button_exit = pygame.transform.scale(self.button_exit,(200,200))
        self.rect_exit = self.button_exit.get_rect()
        self.rect_exit.center = (400,500)
