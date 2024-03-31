import pygame
import math
from jeux import jeux
from Projectile import Projectile

pygame.init()
pygame.display.set_caption("Manifeste") #nom de la fenètre
screen = pygame.display.set_mode((800, 800)) # dimmension de la fenètre

running = True
je = jeux()

clock = pygame.time.Clock() # charge le temps pour l'utiliser dans le jeux
background = pygame.image.load('Asset/Background.png') #charge l'image de l'arrière plan
background = pygame.transform.scale(background, (800,800))
menu_background = pygame.image.load('Asset/Menu/back_menu.png')

projectiles = pygame.sprite.Group()  # Groupe pour stocker les projectiles

while running:
    time = clock.tick(60) / 1000 # Definit le temps

    if je.is_running == False:
        screen.blit(menu_background, (0, 0))
        screen.blit(je.menu.button_start, je.menu.rect_start)
        screen.blit(je.menu.button_exit, je.menu.rect_exit)
        screen.blit(je.menu.button_setting, je.menu.rect_setting)
    else:
        je.start(screen, background, projectiles)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            je.pressed[event.key] = True

            if event.key == pygame.K_SPACE and len(projectiles) < 2:
                # Lancer un nouveau projectile
                new_projectile = Projectile() # Crée une abréviation pour les nouveaux projectile
                new_projectile.rect.center = je.joueur.rect.center
                new_projectile.rect.centerx += int(math.cos(je.projet.angle) * 50)  # Ajuster la position du projectile en fonction de l'angle
                new_projectile.rect.centery -= int(math.sin(je.projet.angle) * 50)  # Ajuster la position du projectile en fonction de l'angle
                new_projectile.velocity_x = math.cos(je.projet.angle) * je.projet.speed # Ajuster la vitesse du projectile
                new_projectile.velocity_y = -math.sin(je.projet.angle) * je.projet.speed # Ajuster la vitesse du projetile
                projectiles.add(new_projectile)

        elif event.type == pygame.KEYUP:
            je.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if je.menu.rect_start.collidepoint(event.pos): #permet l'appuuis du bonton pour staret le jeux
                je.is_running = True
pygame.quit()
