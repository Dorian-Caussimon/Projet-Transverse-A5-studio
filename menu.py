'''
#pour menu
import pygame

# creation de la fenetre
screen = pygame.display.set_mode((1920,1080),(pygame.FULLSCREEN) )


# afficher l'arriere plan de l'ecran d'acceuil.
back = pygame.image.load('Asset/image_jeux.jpg')

# mettre l'ecran
screen.blit(back ,(0,-200))
#rafraichissement de l'ecran
pygame.display.flip()

# importation du bouton
button = pygame.image.load('Asset/play.png')

# a mettre dans le main quand le jeu n'a pas encore commencé
screen.blit(button,(0,0))
button_rect = button.get_rect()

# creation du bouton cliquable

'''



