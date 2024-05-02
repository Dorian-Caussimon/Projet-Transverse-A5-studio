import pygame
import random

pepe = pygame.image.load("Asset/ennemis/Pepe.png")
pepe = pygame.transform.scale(pepe, (100, 100))
joy = pygame.image.load("Asset/ennemis/JoyPepe.png")
joy = pygame.transform.scale(joy, (100, 100))
sad = pygame.image.load("Asset/ennemis/SadPepe.png")
sad = pygame.transform.scale(sad, (100, 100))
ene_list = [sad, pepe, joy]

class ENEMY(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pv_max = random.choice((2,3,4))
        self.pv = self.pv_max
        self.image = ene_list[self.pv_max-2]
        self.rect = pepe.get_rect()
        self.rect.x = 900 + random.randint(0,200)
        self.rect.y = 500 + random.randint(0,100)
        self.pos = 700
        self.vit = 1 + random.randint(0,2)

    def mouv(self):
        self.rect.x -= self.vit

    def pv_bar(self, surface):
        pv = self.pv/self.pv_max
        pygame.draw.rect(surface, "red", (self.rect.x, self.rect.y, 100, 10))
        pygame.draw.rect(surface, "green", (self.rect.x, self.rect.y, 100*pv, 10))