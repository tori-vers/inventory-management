import pygame
import sys
from main import *

WIDTH = 600
HEIGHT = 250

class Display:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Pocket Library")
        self.clock = pygame.time.Clock()
        
        self.library = Inventory()
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            self.screen.fill(gray)
            self.library.run()
            pygame.display.update()
            self.clock.tick()
            
if __name__ == '__main__':
    game = Display()
    game.run()