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

        self.button_menu = pygame.image.load('Asset/Menu/button_menu.png')
        self.button_menu = pygame.transform.scale(self.button_menu,(150,150))
        self.rect_menu = self.button_menu.get_rect()
        self.rect_menu.center = (400,200)

        self.button_resume = pygame.image.load('Asset/Menu/button_resume.png')
        self.button_resume = pygame.transform.scale(self.button_resume,(150,150))
        self.rect_resume = self.button_resume.get_rect()
        self.rect_resume.center = (400,450)

        self.button_restart = pygame.image.load('Asset/Menu/button_restart.png')
        self.button_restart = pygame.transform.scale(self.button_restart,(150,150))
        self.rect_restart = self.button_restart.get_rect()
        self.rect_restart.center = (400,450)