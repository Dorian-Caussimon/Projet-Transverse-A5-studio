import pygame
class joueur(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pv = 5
        self.pv_max = 5
        self.image = pygame.image.load('Asset/Joueur/peso provi.png') # metre skin
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 500