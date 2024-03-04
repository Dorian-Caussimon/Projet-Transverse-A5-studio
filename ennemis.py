import pygame

class ennemi(pygame.sprite.Sprite):
    def __init__(self):
        self.pv = 100
        self.pv_max = 100
        self.image = pygame.image.load('Asset/Joueur/peso provi.png') # metre skin
        self.rect = self.image.get_rect()
        self.x = 900
        self.y = 450
        self.vit = 1/5


    def mouv(self):
        if self.x>10:
            self.x-=self.vit

    def perdu(self):
        if self.x<=10:
            return True
        else:
            return False