import pygame
from pygame.locals import *
import time

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()  # Load the block image
        self.x = 100
        self.y = 100
        self.direction = 'right'
    def draw_block(self):
       
        self.parent_screen.fill((110, 110, 5))
        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()
        
    def move_left(self):
        self.direction = 'left'
        
    def move_right(self):
        self.direction = 'right'
        
    def move_up(self):
        self.direction = 'up'
        
    def move_down(self):
        self.direction = 'down'
        
    def walk(self):
        if self.direction == 'left':
            self.x -= 10
        elif self.direction == 'right':
            self.x += 10
        elif self.direction == 'up':
            self.y -= 10
        elif self.direction == 'down':
            self.y += 10
            
        self.draw_block()
        
class Game:
    
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 500))
        self.surface.fill((110, 110, 5))
        self.snake = Snake(self.surface)
        self.snake.draw_block()
        
    def run(self):
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:  # Exit on Escape
                        running = False
                
                    if event.key == K_UP:  # Move block up
                        self.snake.move_up()
                        
                    if event.key == K_DOWN:  # Move block down (fixed)
                        self.snake.move_down()
                        
                    if event.key == K_LEFT:  # Move block down (fixed)
                        self.snake.move_left()
                        
                    if event.key == K_RIGHT:  # Move block down (fixed)
                        self.snake.move_right()
                        
                    elif event.type == QUIT:  # Exit on close button
                        running = False
                        
            self.snake.walk()
            time.sleep(0.05)
        
if __name__ == "__main__":
    global surface
    game = Game()
    game.run()  
    
    
