import pygame

class ennemi(pygame.sprite.Sprite):
    def __init__(self):
        self.pv = 100
        self.pv_max = 100
        self.image = pygame.image.load('Asset/Joueur/peso provi.png') # metre skin
        self.rect = self.image.get_rect()
        self.rect.x = 900
        self.rect.y = 400
        self.vit = 1/2

    def mouv(self):
        self.rect.x -= self.vit

    def perdu(self):
        if self.rect.x <= 50:
            return True
        return False
