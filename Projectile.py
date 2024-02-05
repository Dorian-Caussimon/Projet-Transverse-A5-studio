import pygame

class projectile(pygame.sprite.Sprite):
    def __init__(self):
        self.velocity = 5
        self.damage = 50
        self.image = pygame.image.load("Asset/Projectile/projectile provisoire.png") #en attente
        self.rect = self.image.get_rect()



