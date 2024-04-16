import pygame
class JOUEUR(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pv_max = 5
        self.pv = self.pv_max
        self.image = pygame.image.load('Asset/Joueur/peso provi.png') # metre skin
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 500

    def pv_bar(self, surface):
        pv = self.pv/self.pv_max
        pygame.draw.rect(surface, "red", (self.rect.x, self.rect.y, 100, 10))
        pygame.draw.rect(surface, "green", (self.rect.x, self.rect.y, 100*pv, 10))