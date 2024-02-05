import pygame
from Joueur import joueur
from ennemis import ennemi
class jeux():
    def __init__(self):
        self.joueur = joueur()
        self.ennemi = ennemi()