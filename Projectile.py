import pygame

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
        self.angle = 1
        self.speed = 5

    def update(self):
        # Mise à jour de la position en fonction des vitesses horizontale et verticale
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
        # Mise à jour de la vitesse verticale en appliquant la gravité
        self.velocity_y += self.gravity

    def increase_speed(self):
        self.speed += 0.1
        if self.speed > 20: # evite un abus de vitesse
            self.speed = 20
    def decrease_speed(self):
        self.speed -= 0.1
        if self.speed < 1 : # evité la vitesse negative
            self.speed = 1
    def increase_angle(self):
        self.angle += 0.01
        if self.angle > 1.4:  # evite d'avoir un angle trop grand
            self.angle = 1.4
    def decrease_angle(self):
        self.angle -= 0.01
        if self.angle < 0.4: # evite d'avoir un angle trop petit
            self.angle = 0.4