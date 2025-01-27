import pygame
from constants import *

class Text():
    def __init__(self, x, y, screen, text):
        self.x = x
        self.y = y
        self.screen = screen
        self.text = text
        self.font = pygame.font.SysFont("freemono", TEXT_SIZE, bold=True)
        self.draw()        

    def update(self, text):
        self.text = text

    def draw(self):
        self.text_surface = self.font.render(self.text, True, TEXT_COLOR)
        self.screen.blit(self.text_surface, (self.x, self.y))


    