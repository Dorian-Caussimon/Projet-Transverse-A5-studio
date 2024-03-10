import pygame
import math
class projectile(pygame.sprite.Sprite):
    def __init__(self,screen):
        super().__init__()
        self.screen = screen
        self.angle = 45
        self.velocity = 100
        self.gravity = 9.8
        self.damage = 50
        self.image = pygame.image.load("Asset/Projectile/projectile provisoire.png") #en attente
        self.rect = self.image.get_rect()
        self.rect.x = 90
        self.rect.y = 400
        self.time = 0
        self.vectx = self.velocity * math.cos(math.radians(self.angle))
        self.vecty = self.velocity * math.sin(math.radians(self.angle))

    def update(self, temps):
        self.time += temps
        self.rect.x += self.vectx * self.time
        self.rect.y += (self.vecty * self.time + 0.5 * self.gravity * self.time ** 2)
        if self.rect.y > 600: # dimmension de la fenètre de jeux
            self.rect.y = 600

    def ajust_angle(self, d):
        self.angle += d
        self.vectx = self.velocity * math.cos(math.radians(self.angle))
        self.vecty = -self.velocity * math.sin(math.radians(self.angle))

    def ajust_vitesse(self, d):
        self.velocity += d
        self.vectx = self.velocity * math.cos(math.radians(self.angle))
        self.vecty = -self.velocity * math.sin(math.radians(self.angle))