import pygame
import random
class ENEMY(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pv = random.choice((2,4))
        self.image = pygame.image.load('Asset/Joueur/peso provi.png') # metre skin
        self.rect = self.image.get_rect()
        self.rect.x = 900 + random.randint(0,200)
        self.rect.y = 500
        self.pos = 700
        self.vit = 1 + random.randint(0,2)

    def mouv(self):
        self.rect.x -= self.vit