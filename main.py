import pygame
from jeux import jeux
from Projectile import projectile

pygame.init()
pygame.display.set_caption("Manifeste")
# dimension de la fenètre

screen = pygame.display.set_mode((1000,600))

#chargment du jeux
running = True

jeux = jeux()

# importer un arrière plan
backgroud = pygame.image.load('Asset/Background.jpg') # en attente de backgroud

# définition du temps
clock = pygame.time.Clock()

#liste pour tout les projectile
projectile_lancer = []

#boucle pour maintenire la fenètre
while running :
    time = clock.tick(60) / 1000 # initialisation du temp

    #affiche background
    screen.blit(backgroud,(0,0))

    # affiche personage
    screen.blit(jeux.joueur.image, jeux.joueur.rect)
    screen.blit(jeux.ennemi.image, jeux.ennemi.rect)

    #mise a jour de l'écrant
    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        # commande pour l'ajustement du projectile
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                projectile_lancer.append(projectile)
            elif event.key == pygame.K_UP:
                for projectile in projectile_lancer:
                    projectile.ajust_angle(5)
            elif event.key == pygame.K_DOWN:
                for projectile in projectile_lancer:
                    projectile.ajust_angle(-5)
            elif event.key == pygame.K_RIGHT:
                for projectile in projectile_lancer:
                    projectile.ajust_vitesse(5)
            elif event.key == pygame.K_LEFT:
                for projectile in projectile_lancer:
                    projectile.ajust_vitesse(-5)

    for p in projectile_lancer:
        projectile.update(time)
        projectile.draw()

    # mise a jour de l'affichage
    pygame.display.flip()

pygame.quit()