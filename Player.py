import pygame

joueur = pygame.image.load("Asset/Joueur/SamuDoge.png")
joueur = pygame.transform.scale(joueur, (200, 200))
class JOUEUR(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pv_max = 5
        self.pv = self.pv_max
        self.image = joueur
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 500

    def pv_bar(self, surface):
        pv = self.pv/self.pv_max
        pygame.draw.rect(surface, "red", (self.rect.x, self.rect.y, 200, 10))
        pygame.draw.rect(surface, "green", (self.rect.x, self.rect.y, 200*pv, 10))