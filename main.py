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

projectiles = pygame.sprite.Group()  # Groupe pour stocker les projectiles

launch_angle = je.joueur.angle  # Angle initial
launch_speed = je.joueur.speed  # Vitesse initiale

while running:
    time = clock.tick(60) / 1000 # Definit le temps
    screen.blit(background, (0, 0))

    screen.blit(je.joueur.image, je.joueur.rect) # affiche le joueur
    screen.blit(je.ennemi.image, je.ennemi.rect) # affiche les énemie



    # Dessiner la ligne d'indicateur de lancement
    start_pos = je.joueur.rect.center
    end_pos = (start_pos[0] + int(math.cos(launch_angle) * launch_speed * 10), start_pos[1] - int(math.sin(launch_angle) * launch_speed * 10))
    pygame.draw.line(screen, (255, 0, 0), start_pos, end_pos, 2)

    for projectile in projectiles:
        projectile.update() # met a jour la possition du projectile
        screen.blit(projectile.image, projectile.rect) # met a jour l'écrant pour afficher le projectile

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                # Lancer un nouveau projectile
                new_projectile = Projectile() # Crée une abréviation pour les nouveaux projectile
                new_projectile.rect.center = je.joueur.rect.center
                new_projectile.rect.centerx += int(math.cos(launch_angle) * 50)  # Ajuster la position du projectile en fonction de l'angle
                new_projectile.rect.centery -= int(math.sin(launch_angle) * 50)  # Ajuster la position du projectile en fonction de l'angle
                new_projectile.velocity_x = math.cos(launch_angle) * launch_speed # Ajuster la vitesse du projectile
                new_projectile.velocity_y = -math.sin(launch_angle) * launch_speed # Ajuster la vitesse du projetile
                projectiles.add(new_projectile)

            elif event.key == pygame.K_UP:
                # Augmenter la puissance de lancer
                launch_speed += 1

            elif event.key == pygame.K_DOWN:
                # Diminuer la puissance de lancer
                launch_speed -= 1
                if launch_speed < 1:
                    launch_speed = 1  # Assure que la puissance ne devienne pas négative

            elif event.key == pygame.K_RIGHT:
                # Augmenter l'angle
                launch_angle += 0.1

            elif event.key == pygame.K_LEFT:
                # Diminuer l'angle
                launch_angle -= 0.1

pygame.quit()
