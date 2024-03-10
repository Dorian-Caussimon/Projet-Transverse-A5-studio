import pygame
import math

class Projectile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.damage = 50
        self.image = pygame.image.load("Asset/Projectile/projectile provisoire.png")  # Image du projectile (à remplacer)
        self.rect = self.image.get_rect()
        self.rect.x = 90
        self.rect.y = 400
        self.velocity_x = 0  # Vitesse horizontale du projectile
        self.velocity_y = 0  # Vitesse verticale du projectile
        self.gravity = 0.5  # Gravité appliquée au projectile

    def update(self):
        # Mise à jour de la position en fonction des vitesses horizontale et verticale
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
        # Mise à jour de la vitesse verticale en appliquant la gravité
        self.velocity_y += self.gravity
