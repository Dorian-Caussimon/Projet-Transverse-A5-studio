import math
import pygame
from pygame import sprite

from Player import JOUEUR
from enemy import ENEMY
from menu import menu
from Projectile import PROJECTILE
import random

class GAME():
    def __init__(self):
        self.is_menu = True
        self.is_running = False
        self.is_posing = False
        self.is_game_over = False
        self.projet = PROJECTILE()  # récupère la classe Projectile
        self.joueur = JOUEUR()  # récupère la classe joueur
        self.ennemi = ENEMY()  # récupère la classe ENNEMIE
        self.menu = menu()  # récupère la classe menu
        self.proj_group = pygame.sprite.Group()
        self.pressed = {}
        #groupe d'Enemy
        self.enemy_group = pygame.sprite.Group()

    def spawn_enemy(self):
        enemy = ENEMY()
        self.enemy_group.add(enemy)
    def start(self, screen, background, projectiles_group):
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


        for proj in projectiles_group:
            proj.update()  # met a jour la possition du projectile
            screen.blit(proj.image, proj.rect)  # met a jour l'écrant pour afficher le projectile

            if proj.rect.x > 800 or proj.rect.y > 800:  # supprime le projetile si il sort de l'écrant
                projectiles_group.remove(proj)

        if len(self.enemy_group) < 2:
            self.spawn_enemy()
        self.enemy_group.draw(screen) # affiche les enemie

        for ene in self.enemy_group:
            ene.mouv()
            if ene.rect.x < 0:
                self.enemy_group.remove(ene)
            if ene.rect.colliderect(self.joueur.rect):
                self.enemy_group.remove(ene)
            for proj in projectiles_group:
                if ene.rect.colliderect(proj):
                    ene.pv -= 1
                    projectiles_group.remove(proj)
                if ene.rect.colliderect(proj) and ene.pv == 0:
                    self.enemy_group.remove(ene)


        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                self.pressed[event.key] = True

                if event.key == pygame.K_ESCAPE:
                    self.is_posing = True
                    self.is_running = False

                if event.key == pygame.K_SPACE and len(projectiles_group) < 2:  # faire un cooldown --------------------------------------------------------------------
                    # Lancer un nouveau projectile
                    new_projectile = PROJECTILE()  # Crée une instance pour les nouveaux projectile
                    new_projectile.rect.center = self.joueur.rect.center
                    new_projectile.rect.centerx += int(math.cos(self.projet.angle) * 50)  # Ajuster la position du projectile en fonctionl'angle
                    new_projectile.rect.centery -= int(math.sin(self.projet.angle) * 50)  # Ajuster la position du projectile en fonction de l'angle
                    new_projectile.velocity_x = math.cos(self.projet.angle) * self.projet.speed  # Ajuster la vitesse du projectile
                    new_projectile.velocity_y = - math.sin(self.projet.angle) * self.projet.speed  # Ajuster la vitesse du projetile
                    projectiles_group.add(new_projectile)

            elif event.type == pygame.KEYUP:
                self.pressed[event.key] = False







    
    def interface_menu(self, screen, menu_background):
        screen.blit(menu_background, (0, 0))
        screen.blit(self.menu.button_start, self.menu.rect_start)
        screen.blit(self.menu.button_exit, self.menu.rect_exit)
        screen.blit(self.menu.button_setting, self.menu.rect_setting)

        while self.is_menu == True:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.menu.rect_start.collidepoint(event.pos):  # permet l'appuuis du bonton pour start le jeux
                        self.is_running = True
                        self.is_menu = False

                    elif self.menu.rect_exit.collidepoint(event.pos):  # permet l'appuuis du bonton pour quiter le jeux
                        pygame.quit()
    def interface_pause(self, screen, menu_background):
        screen.blit(menu_background, (0, 0))
        screen.blit(self.menu.button_resume, self.menu.rect_resume)
        screen.blit(self.menu.button_menu, self.menu.rect_menu)

        while self.is_posing == True:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.type == pygame.MOUSEBUTTONDOWN:

                        if self.menu.rect_resume.collidepoint(event.pos):  # permet l'appuuis du bonton pour retourner dans le jeux
                            self.is_posing = False
                            self.is_running = True

                        elif self.menu.rect_menu.collidepoint(event.pos):  # permet l'appuis du bouton pour retourner au menu
                            self.is_posing = False
                            self.is_menu = True
    def interface_game_over(self, screen, menu_background):
        screen.blit(menu_background, (0, 0))
        screen.blit(self.menu.button_restart, self.menu.rect_resume)
        screen.blit(self.menu.button_menu, self.menu.rect_menu)

        while self.is_game_over == True:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.menu.rect_restart.collidepoint(event.pos):  # permet l'appuuis du bonton pour restart le jeux
                        self.is_running = True
                        self.is_game_over = False

                    elif self.menu.rect_menu.collidepoint(event.pos):  # permet l'appuis du bouton pour retourner au menu
                        self.is_running = False
                        self.is_game_over = False