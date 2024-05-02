import pygame
import math
from Game import GAME
from Projectile import PROJECTILE as PO

pygame.init()
pygame.display.set_caption("A5-Studio") #nom de la fenètre
screen = pygame.display.set_mode((800, 800)) # dimmension de la fenètre
running = True

je = GAME()

clock = pygame.time.Clock() # charge le temps pour l'utiliser dans le jeux
background = pygame.image.load('Asset/Background.png') #charge l'image de l'arrière plan
background = pygame.transform.scale(background, (800,800))
menu_background = pygame.image.load('Asset/Menu/Menu.png')
menu_background = pygame.transform.scale(menu_background, (800, 800))

proj_group = pygame.sprite.Group()  # Groupe pour stocker les proj_group
enemy_group = pygame.sprite.Group()

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

pygame.quit()