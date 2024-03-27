import pygame
import math
class joueur(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pv = 100
        self.pv_max = 100
        self.image = pygame.image.load('Asset/Joueur/peso provi.png') # metre skin
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 500
        self.angle = (math.pi / 4)
        self.speed = 5