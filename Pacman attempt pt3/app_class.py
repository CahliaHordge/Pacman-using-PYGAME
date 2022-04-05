import pygame
from settings import *
import sys


pygame.init()
vec = pygame.math.Vector2


class App:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'

    def run(self):
        while self.running:
            if self.state == 'start':
                self.intro_events()
                self.intro_update()
                self.intro_draw
            else:
                pass
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()
######################## Help Functions ################################



######################## INTRO FUNCTIONS ################################

    def intro_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'
    def start_update(self):
        pass

    def start_draw(self):
        self.screen.fill(BLACK)
        self.draw_text(self.screen,START_TEXT_SIZE,(170, 132,50))
        pygame.display.update()