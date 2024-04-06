import math
import pygame
from Joueur import joueur
from ennemis import ennemi
from menu import menu
from Projectile import Projectile

class jeux():
    def __init__(self):
        self.is_running = False
        self.projet = Projectile()
        self.joueur = joueur() # récupère la classe joueur
        self.ennemi = ennemi() # récupère la classe ennemi
        self.menu = menu() # récupère la classe menu
        self.pressed = {}

    def start(self,screen,background,projectiles):
        screen.blit(background, (0, 0))  # affiche l'arrière plan
        screen.blit(self.joueur.image, self.joueur.rect)  # affiche le joueur
        screen.blit(self.ennemi.image, self.ennemi.rect)  # affiche les énemie

        # modification de la puissance et de l'angle du projectile
        if self.pressed.get(pygame.K_RIGHT):
            self.projet.decrease_angle()  # Diminuer l'angle
        elif self.pressed.get(pygame.K_LEFT):
            self.projet.increase_angle()  # augmante l'angle
        elif self.pressed.get(pygame.K_UP):
            self.projet.increase_speed()  # Augmenter la puissance de lancer
        elif self.pressed.get(pygame.K_DOWN):
            self.projet.decrease_speed()  # Diminuer la puissance de lancer

        # Dessiner la ligne d'indicateur de lancement
        start_pos = self.joueur.rect.center
        end_pos = (start_pos[0] + int(math.cos(self.projet.angle) * self.projet.speed * 10),
                   start_pos[1] - int(math.sin(self.projet.angle) * self.projet.speed * 10))
        pygame.draw.line(screen, (255, 0, 0), start_pos, end_pos, 2)

        for projectile in projectiles:
            projectile.update()  # met a jour la possition du projectile
            screen.blit(projectile.image, projectile.rect)  # met a jour l'écrant pour afficher le projectile