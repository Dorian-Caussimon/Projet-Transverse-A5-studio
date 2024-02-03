import pygame

class joueur :
    def _init_(self):
        self.health = 100

pygame.init()
pygame.display.set_caption("Manifeste")
screen = pygame.display.set_mode((1920,1080))
running = True

# importer un arrière plan
#backgroud = pygame.image.load('Asset')

#boucle pour maintenire la fenètre
while running :

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False