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
        self.cell_width = MAZE_WIDTH//28
        self.cell_height = MAZE_HEIGHT//30
        
        self.load()

        
    def run(self):
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.start_update()
                self.start_draw()
            elif self.state == 'playing':
                 self.playing_events()
                 self.playing_update()
                 self.playing_draw()
            else:
                self.clock.tick(FPS)
        pygame.quit()
        sys.exit()


######################## Help Functions ################################
    def draw_text(self, words, screen, pos, size,
     color, font_name, centered=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, color)
        text_sixe = text.get_size()
        if centered:
            pos[0] = pos[0]-text_sixe[0]//2
            pos[1] = pos[1]-text_sixe[1]//2
        screen.blit(text, pos)
    
    def load(self): 
        self.background = pygame.image.load('maze.png')
        self.background = pygame.transform.scale(self.background,
        (MAZE_WIDTH, MAZE_HEIGHT))
    
    def draw_grid(self):
            for x in range (WIDTH//self.cell_width):
                pygame.draw.line(self.background, GREY, (x*self.cell_width, 0),
                 (x*self.cell_width, HEIGHT))
            for x in range (HEIGHT//self.cell_height):
                pygame.draw.line(self.background, GREY,(0,x*self.cell_height),(WIDTH, x*self.cell_height))
######################## INTRO FUNCTIONS ################################

    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'
    
    def start_update(self):
        pass


    def start_draw(self):
        self.screen.fill(BLACK)
        self.draw_text('PUSH SPACE BAR',self.screen,[WIDTH//2, HEIGHT//2-50],
        START_TEXT_SIZE,(170, 132,50), START_FONT, centered=True)
        self.draw_text('1 PLAYER ONLY',self.screen,[WIDTH//2, HEIGHT//2+50],
        START_TEXT_SIZE,(44, 167, 198), START_FONT, centered=True)
        self.draw_text('HIGH SCORE',self.screen,[4,0],
        START_TEXT_SIZE,(255,255,255), START_FONT)
        pygame.display.update()

######################## Playing FUNCTIONS ################################

    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    def playing_update(self):
        pass


    def playing_draw(self):
        self.screen.blit(self.background,(TOP_BOTTOM_BUFFER//2, 
        TOP_BOTTOM_BUFFER//2))
        self.draw_grid()
        self.draw_text(self, 'HIGH SCORE: 0', self.screen, (10,5), 18, WHITE, 
        START_FONT)
        pygame.display.update()
        
