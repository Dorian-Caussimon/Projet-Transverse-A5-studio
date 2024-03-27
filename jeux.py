import pygame
from Joueur import joueur
from ennemis import ennemi
from menu import menu

class jeux():
    def __init__(self):
        self.joueur = joueur()
        self.ennemi = ennemi()
        self.menu = menu()
