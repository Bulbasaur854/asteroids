import pygame

class Score():
    def __init__(self, screen):
        self.score = 0
        self.screen = screen
        self.font = pygame.font.SysFont("freemono", 30, bold=True)
        self.draw_score()

    def update_score(self, score):
        self.score += score

    def draw_score(self):
        self.text_surface = self.font.render(f"{self.score}", True, (0,255,0))
        self.screen.blit(self.text_surface, (24, 24))

    def get_score(self):
        return self.score