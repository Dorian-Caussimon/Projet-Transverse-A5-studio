import pygame
from jeux import jeux


pygame.init()
pygame.display.set_caption("Manifeste")
# dimension de la fenètre

screen = pygame.display.set_mode((1000,600))

#chargment du jeux
running = True

jeux = jeux()

# importer un arrière plan
backgroud = pygame.image.load('Asset/Background.jpg') # en attente de backgroud


#boucle pour maintenire la fenètre
while running :
    while jeux.ennemi.perdu() == False:
        #affiche background
        screen.blit(backgroud,(0,0))

        # affiche personage
        screen.blit(jeux.joueur.image, jeux.joueur.rect)

        #affichage des ennemis
        screen.blit(jeux.ennemi.image, (jeux.ennemi.x, jeux.ennemi.y))
        jeux.ennemi.mouv()

        # affiche projectile
        jeux.joueur.projectiles.draw(screen)
        for projectile in jeux.joueur.projectiles :
            projectile.mouvement()
        #mise a jour de l'écrant
        pygame.display.flip()

    #game over
    screen.fill((0, 0, 0))
    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jeux.joueur.projectile()