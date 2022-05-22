import sys
import pygame
import random
from pygame.math import Vector2

DISPLAY_WIDTH_HEIGHT = (400, 500)
SURFACE_WIDTH_HEIGHT = (100, 200)
FRAMERATE = 60
SURFACE_COLOR = (0, 37, 84) # color name: Sköldgul
FRUIT_COLOR = (207, 181, 113)
SNAKE_COLOR_YELLOW = (255, 236, 13)
SNAKE_COLOR_RED = (226, 31, 36)
SNAKE_COLOR_BLUE = (5, 104, 175)
CELL_SIZE = 40
CELL_NUMBER = 20



class Fruit:
    def __init__(self) -> None:
        # create an x and y pos for fruit
        self.x = random.randint(0, CELL_NUMBER-1) # minus 1 due to top left placement
        self.y = random.randint(0, CELL_NUMBER-1) # minus 1 due to top left placement
        self.pos = Vector2(self.x, self.y)
        
        #draw a square
    def draw_fruit(self):
        # create a rectangle
        fruit_rect = pygame.Rect(int(self.pos.x*CELL_SIZE), int(self.pos.y*CELL_SIZE), CELL_SIZE, CELL_SIZE)
        # draw the rectangle
        pygame.draw.rect(screen, FRUIT_COLOR, fruit_rect)

class Snake:
    def __init__(self) -> None:
        self.body = [Vector2(5,10), Vector2(6,10), Vector2(7,10)]
        self.direction = Vector2(1,0)
    
    def draw_snake(self):
        i = 0
        for block in self.body:

            #create rectangle'
            x_pos = int(block.x*CELL_SIZE)
            y_pos = int(block.y*CELL_SIZE)
            snake_draw = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
            #draw rectangle
            if i % 3 == 0:
                pygame.draw.rect(screen, SNAKE_COLOR_YELLOW, snake_draw)
            if i % 3 == 1:
                pygame.draw.rect(screen, SNAKE_COLOR_RED, snake_draw)
            if i % 3 == 2:
                pygame.draw.rect(screen, SNAKE_COLOR_BLUE, snake_draw)
            i += 1
    
    def move_snake(self):
        body_copy = self.body[:-1] # all body vectors except the last. last part of the tale disapears
        body_copy.insert(0, body_copy[0]+self.direction) # move head
        self.body = body_copy[:]


pygame.init()


screen = pygame.display.set_mode((CELL_NUMBER*CELL_SIZE, CELL_NUMBER*CELL_SIZE))
clock = pygame.time.Clock()

fruit = Fruit()
snake = Snake()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Vi älsker Djurgården")
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            snake.move_snake()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                snake.direction = Vector2(0,1)
            if event.key == pygame.K_RIGHT:
                snake.direction = Vector2(1,0)
            if event.key == pygame.K_LEFT:
                snake.direction = Vector2(-1,0)
            
        
    
    screen.fill(SURFACE_COLOR)
    fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(FRAMERATE)