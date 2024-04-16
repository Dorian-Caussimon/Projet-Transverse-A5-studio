import pygame
import math
from jeux import jeux
from Projectile import Projectile as PO

pygame.init()
pygame.display.set_caption("A5-Studio") #nom de la fenètre
screen = pygame.display.set_mode((800, 800)) # dimmension de la fenètre

running = True
je = jeux()

clock = pygame.time.Clock() # charge le temps pour l'utiliser dans le jeux
background = pygame.image.load('Asset/Background.png') #charge l'image de l'arrière plan
background = pygame.transform.scale(background, (800,800))
menu_background = pygame.image.load('Asset/Menu/back_menu.png')

proj_group = pygame.sprite.Group()  # Groupe pour stocker les proj_group

while running:
    clock.tick(60)

    pygame.display.flip()
    if je.is_menu == True:
        je.interface_menu(screen, menu_background)
    elif je.is_posing == True:
        je.interface_pause(screen, menu_background)
    elif je.is_running == True:
        je.start(screen, background, proj_group)
    elif je.is_game_over == True:
        je.interface_game_over(screen, menu_background)

    print('menu:{} posing:{} running:{} game over:{}'.format(je.is_menu,je.is_posing,je.is_running,je.is_game_over))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            je.pressed[event.key] = True

            if event.key == pygame.K_ESCAPE:
                je.is_posing = True
                je.is_running = False

            if event.key == pygame.K_SPACE and len(proj_group) < 2: # faire un cooldown --------------------------------------------------------------------
                # Lancer un nouveau projectile
                new_projectile = PO() # Crée une instance pour les nouveaux projectile
                new_projectile.rect.center = je.joueur.rect.center
                new_projectile.rect.centerx += int(math.cos(je.projet.angle) * 50)  # Ajuster la position du projectile en fonction de l'angle
                new_projectile.rect.centery -= int(math.sin(je.projet.angle) * 50)  # Ajuster la position du projectile en fonction de l'angle
                new_projectile.velocity_x = math.cos(je.projet.angle) * je.projet.speed # Ajuster la vitesse du projectile
                new_projectile.velocity_y = - math.sin(je.projet.angle) * je.projet.speed # Ajuster la vitesse du projetile
                proj_group.add(new_projectile)

        elif event.type == pygame.KEYUP:
            je.pressed[event.key] = False
pygame.quit()
