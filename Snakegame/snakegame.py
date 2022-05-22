import sys
import pygame
import random
import time
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
go = True

class Fruit:
    def __init__(self) -> None:
        # create an x and y pos for fruit
        self.randomize()
        
        #draw a square
    def draw_fruit(self):
        # create a rectangle
        fruit_rect = pygame.Rect(int(self.pos.x*CELL_SIZE), int(self.pos.y*CELL_SIZE), CELL_SIZE, CELL_SIZE)
        # draw the rectangle
        pygame.draw.rect(screen, FRUIT_COLOR, fruit_rect)
    
    def randomize(self):
        self.x = random.randint(0, CELL_NUMBER-1) # minus 1 due to top left placement
        self.y = random.randint(0, CELL_NUMBER-1) # minus 1 due to top left placement
        self.pos = Vector2(self.x, self.y)

class Snake:
    def __init__(self) -> None:
        self.body = [Vector2(CELL_NUMBER/2,CELL_NUMBER/2), Vector2((CELL_NUMBER/2)-1,CELL_NUMBER/2), Vector2((CELL_NUMBER/2)-2,CELL_NUMBER/2)]
        self.direction = Vector2(1,0)
        self.new_block = False
    
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
        if self.new_block == True:
            body_copy = self.body[:] # all body vectors except the last. last part of the tale disapears
            body_copy.insert(0, body_copy[0]+self.direction) # move head
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1] # all body vectors except the last. last part of the tale disapears
            body_copy.insert(0, body_copy[0]+self.direction) # move head
            self.body = body_copy[:]
    
    def add_block(self):
        self.new_block = True

class Main:
    def __init__(self) -> None:
        self.snake = Snake()
        self.fruit = Fruit()
    
    def update(self):
        self.snake.move_snake()
    
    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
    
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            check = True
            print("nam nam")
            #self.fruit = Fruit()
            self.fruit.randomize()
            while check:
                for block in self.snake.body[:]:
                    if block == self.fruit.pos:
                        self.fruit.randomize()
                check = False      
            self.snake.add_block()
    
    def check_fail(self):
        # check oustide of display
        if self.snake.body[0].x<0:
            print("fail vänster")
            self.game_over()
        if self.snake.body[0].y<0:
            print("fail uppe")
            self.game_over()
        if self.snake.body[0].x>CELL_NUMBER:
            print("fail höger")
            self.game_over()
        if self.snake.body[0].y>CELL_NUMBER:
            print("fail nere")
            self.game_over()
        # check if head hits body
        for i in self.snake.body[1:]:
            if self.snake.body[0] == i:
                print("krock med dig själv")
                self.game_over()
    
    def game_over(self):
        time.sleep(3)
        pygame.quit() # deactivates the pygame library
        sys.exit() # quit the program.
    

pygame.init()
screen = pygame.display.set_mode((CELL_NUMBER*CELL_SIZE, CELL_NUMBER*CELL_SIZE))
clock = pygame.time.Clock()
pygame.display.set_caption('Snake vs råtta')

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = Main() # Create a snake and fruit

while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Vi älsker Djurgården")
            pygame.quit() # deactivates the pygame library
            sys.exit() # quit the program.
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)
            

    screen.fill(SURFACE_COLOR)
    main_game.draw_elements()
    main_game.check_collision()
    main_game.check_fail()
    pygame.display.update() # Draws the surface object to the screen.
    clock.tick(FRAMERATE)
