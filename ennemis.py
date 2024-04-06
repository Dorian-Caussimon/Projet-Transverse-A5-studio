import pygame

class ennemi(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pv = 100
        self.pv_max = 100
        self.image = pygame.image.load('Asset/Joueur/peso provi.png') # metre skin
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 500
        self.pos = 700
        self.vit = 1

    def mouv(self):
        self.pos -= self.vit
        self.rect.x = self.pos

    def spawn_ennemi(self):
        self.pos = 1000
        self.rect.x = self.pos
        self.pv = self.pv_max