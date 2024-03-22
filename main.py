import pygame
import math
from Jeux import jeux
from Projectile import Projectile

pygame.init()
pygame.display.set_caption("Manifeste") #nom de la fenètre
screen = pygame.display.set_mode((1000, 600)) # dimmension de la fenètre

running = True
jeu = jeux()

clock = pygame.time.Clock() # charge le temps pour l'utiliser dans le jeux
background = pygame.image.load('Asset/Background.jpg') #charge l'image de l'arrière plan
projectiles = pygame.sprite.Group()  # Groupe pour stocker les projectiles

launch_angle = jeu.joueur.angle  # Angle initial
launch_speed = jeu.joueur.speed  # Vitesse initiale

font = pygame.font.Font(None, 30)  # Police de caractères pour afficher les informations

while running:
    time = clock.tick(60) / 1000
    screen.blit(background, (0, 0))
    screen.blit(jeu.joueur.image, jeu.joueur.rect)
    screen.blit(jeu.ennemi.image, jeu.ennemi.rect)

    #déplacement de l'ennemi
    jeu.ennemi.mouv()

    # Dessiner la ligne d'indicateur de lancement
    start_pos = jeu.joueur.rect.center
    end_pos = (start_pos[0] + int(math.cos(launch_angle) * launch_speed * 10), start_pos[1] - int(math.sin(launch_angle) * launch_speed * 10))
    pygame.draw.line(screen, (255, 0, 0), start_pos, end_pos, 2)

    for projectile in projectiles:
        projectile.update()
        screen.blit(projectile.image, projectile.rect)


    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Lancer un nouveau projectile
                new_projectile = Projectile()
                new_projectile.rect.center = jeu.joueur.rect.center
                new_projectile.rect.centerx += int(math.cos(launch_angle) * 50)  # Ajuster la position du projectile en fonction de l'angle
                new_projectile.rect.centery -= int(math.sin(launch_angle) * 50)  # Ajuster la position du projectile en fonction de l'angle
                new_projectile.velocity_x = math.cos(launch_angle) * launch_speed
                new_projectile.velocity_y = -math.sin(launch_angle) * launch_speed
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
