import pygame
import sys
from projectile import Projectile

# Initialisation de Pygame
pygame.init()

# Définition de quelques constantes
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Création de la fenêtre Pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Projectile Motion")

# Font pour le texte
font = pygame.font.Font(None, 36)

# Fonction pour afficher le texte
def show_text(text, x, y):
    text_surface = font.render(text, True, BLACK)
    screen.blit(text_surface, (x, y))

# Boucle de jeu
clock = pygame.time.Clock()

launched_projectiles = []

running = True
while running:
    dt = clock.tick(60) / 1000  # Delta de temps en secondes

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                launched_projectiles.append(Projectile(screen))  # Ajouter un nouveau projectile
            elif event.key == pygame.K_UP:
                for projectile in launched_projectiles:
                    projectile.adjust_angle(5)
            elif event.key == pygame.K_DOWN:
                for projectile in launched_projectiles:
                    projectile.adjust_angle(-5)
            elif event.key == pygame.K_RIGHT:
                for projectile in launched_projectiles:
                    projectile.adjust_speed(5)
            elif event.key == pygame.K_LEFT:
                for projectile in launched_projectiles:
                    projectile.adjust_speed(-5)

    # Effacer l'écran
    screen.fill(WHITE)

    # Mettre à jour et dessiner tous les projectiles lancés
    for projectile in launched_projectiles:
        projectile.update(dt)
        projectile.draw()

    # Afficher les paramètres actuels
    show_text(f"Press SPACE to launch a projectile", 20, 20)
    show_text(f"Press UP/DOWN to adjust angle", 20, 60)
    show_text(f"Press LEFT/RIGHT to adjust speed", 20, 100)

    # Mettre à jour l'affichage
    pygame.display.flip()

pygame.quit()
sys.exit()
