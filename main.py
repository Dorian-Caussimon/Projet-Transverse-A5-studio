import pygame
from jeux import jeux

class joueur :
    def _init_(self):
        self.health = 100

class ennemi :
    def _init_(self):
        self.health = 100

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