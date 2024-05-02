import pygame
import random
class ENEMY(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pv_max = random.choice((2,4))
        self.pv = self.pv_max
        self.image = pygame.image.load('Asset/ennemis/peso provi.png') # metre skin
        self.rect = self.image.get_rect()
        self.rect.x = 900 + random.randint(0,200)
        self.rect.y = 500
        self.pos = 700
        self.vit = 1 + random.randint(0,2)

    def mouv(self):
        self.rect.x -= self.vit

    def pv_bar(self, surface):
        pv = self.pv/self.pv_max
        pygame.draw.rect(surface, "red", (self.rect.x, self.rect.y, 100, 10))
        pygame.draw.rect(surface, "green", (self.rect.x, self.rect.y, 100*pv, 10))