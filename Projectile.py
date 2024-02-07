import pygame

class projectile(pygame.sprite.Sprite):
    def __init__(self,player):
        super().__init__()
        self.velocity = 2
        self.damage = 50
        self.image = pygame.image.load("Asset/Projectile/projectile provisoire.png") #en attente
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 80
        self.rect.y = player.rect.y

    def mouvement(self):
        self.rect.x += self.velocity
