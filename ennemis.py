import pygame

class ennemi(pygame.sprite.Sprite):
    def __init__(self):
        self.pv = 100
        self.pv_max = 100
        self.image = pygame.image.load('Asset/Joueur/peso provi.png') # metre skin
        self.rect = self.image.get_rect()
        self.rect.x = 900
        self.rect.y = 500
        self.vit = 3