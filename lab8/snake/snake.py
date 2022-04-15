import pygame as pg
from random import randint
import time

pg.init()

def drawGrid():
    for x in range(0, width, block_size):
        for y in range(0, height, block_size):
            rect = pg.Rect(x, y, block_size, block_size)
            pg.draw.rect(screen, (50, 50, 100), rect, 1)

def you_won():
    screen.fill((0, 0, 0))
    text = font1.render('YOU WON!', True, (255, 0, 255))
    text1 = font1.render(f'Level: {level.level_count}', True, (255, 0, 255))
    text2 = font1.render(f'Score: {cnt}', True, (255, 0, 255))
    screen.blit(text, (120, 180))
    screen.blit(text1, (150, 240))
    screen.blit(text2, (150, 270))
    pg.display.update()

def game_over():
    screen.fill((0, 0, 0))
    text = font1.render('SAD...', True, (255, 0, 255))
    text1 = font1.render(f'Level: {level.level_count}', True, (255, 0, 255))
    text2 = font1.render(f'Score: {cnt}', True, (255, 0, 255))
    screen.blit(text, (165, 180))
    screen.blit(text1, (150, 240))
    screen.blit(text2, (150, 270))
    pg.display.update()
class level_and_cnt: #remembers and shows the current level and score
    def __init__(self, level):
        self.level_count = level
        self.cnt = 0

    def draw(self, cnt):
        self.cnt = cnt
        font = pg.font.SysFont('Verdana', 15)
        text = font.render(f'Level: {self.level_count} Score: {self.cnt}', True, (255, 255, 255))
        screen.blit(text, (10, 370))

class Snake(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.body = [[10, 10]]
        self.dx = 0
        self.dy = 0

    def move(self): #motion of the snake
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i][0] = self.body[i-1][0]
            self.body[i][1] = self.body[i-1][1]

        self.body[0][0] += self.dx 
        self.body[0][1] += self.dy 

        if self.body[0][0] * block_size > width - 1:
            self.body[0][0] = 0
        if self.body[0][1] * block_size > height - 1:
            self.body[0][1] = 0
        if self.body[0][0] < 0:
            self.body[0][0] = width / block_size
        if self.body[0][1] < 0:
            self.body[0][1] = height / block_size
        
        for i in range(len(self.body) - 1, 0, -1):
            if self.body[0][0] == self.body[i][0]:
                if self.body[0][1] == self.body[i][1]:
                    run = not run
                    
    def check_collision(self, food): #checks whether snake picks up the food
        global cnt
        point = self.body[0]
        a, b = food.rect.topleft
        if point[0] * block_size == a and point[1] * block_size == b:
            self.body.append([a, b])
            food.change_location()
            cnt += 1

    def draw(self): #draws the snake (head and body separately)
        point = self.body[0]
        rect = pg.Rect(block_size * point[0], block_size * point[1], block_size, block_size)
        pg.draw.rect(screen, (128, 0, 255), rect)

        for point in self.body[1:]:
            rect = pg.Rect(block_size * point[0], block_size * point[1], block_size, block_size)
            pg.draw.rect(screen, (50, 128, 128), rect)

class Food(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surface = pg.Surface((block_size, block_size))
        self.surface.fill((0, 255, 0))
        self.rect = self.surface.get_rect(topleft = (block_size * randint(0, 19), block_size * randint(0, 19)))
    
    def change_location(self):
        self.rect.topleft = (block_size * randint(0, 19), block_size * randint(0, 19))

    def not_in_wall(self, wall):
        wall_coordinates = []
        a, b = self.rect.topleft
        for border in wall.body:
            x = border[0] * block_size
            y = border[1] * block_size
            wall_coordinates.append([x, y])
        if [a, b] in wall_coordinates:
            return False
        return True

    def not_in_snake(self, snake):
        snake_coordinates = []
        a, b = self.rect.topleft
        for body in snake.body:
            x = body[0] * block_size
            y = body[1] * block_size
            snake_coordinates.append([x, y])
        if [a, b] in snake_coordinates:
            return False
        return True

    def draw(self):
        screen.blit(self.surface, self.rect)

class Wall(pg.sprite.Sprite):
    def __init__(self, level): #initializing the wall by using txt file
        super().__init__()
        self.body = []
        f = open("level/L{}.txt".format(level), "r")

        for y in range(0, height//block_size + 1):
            for x in range(0, width//block_size + 1):
                if f.read(1) == '#':
                    self.body.append([x, y])

    def collision(self, snake): #checks whether snake collided in the wall
        a, b = snake.body[0]
        for border in wall.body:
            if border[0] == a and border[1] == b:
                game_over(level)
                time.sleep(2)
                run = not run

    def draw(self): #draws the wall on the screen
        for point in self.body:
            rect = pg.Rect(block_size * point[0], block_size * point[1], block_size, block_size)
            pg.draw.rect(screen, (255, 0, 255), rect)


height, width = 420, 420
cnt, lvl = 0, 1
block_size = 20
run = True

pg.display.set_caption('Snake')
screen = pg.display.set_mode((width, height))
screen.fill((0, 0, 0))
clock = pg.time.Clock()

font1 = pg.font.SysFont('Verdana', 30)
#initializing all the classes
snake = Snake()
food = Food()
wall = Wall(lvl)
level = level_and_cnt(lvl)
win_score = [1, 1, 1, 1] #the score that player need to get to pass the level
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = not run
        if event.type == pg.KEYDOWN: #changes the direction by arrow clicks
            if event.key == pg.K_RIGHT:
                snake.dx = 1
                snake.dy = 0
            if event.key == pg.K_LEFT:
                snake.dx = -1
                snake.dy = 0
            if event.key == pg.K_UP:
                snake.dx = 0
                snake.dy = -1
            if event.key == pg.K_DOWN:
                snake.dx = 0
                snake.dy = 1

    snake.move() #changes the location of the snake
    wall.collision(snake) #stops the game if snake collided in the wall
    snake.check_collision(food) #food eating and snake's growth

    while not food.not_in_wall(wall): #makes sure the food isn't spawned in the wall
        food.change_location()

    while not food.not_in_snake(snake): #makes sure the food isn't spawned in the snake's body
        food.change_location()

    if len(snake.body) > win_score[lvl - 1]:
        lvl += 1
        if lvl == 5: 
            you_won()
            time.sleep(2)
            run = not run 
        snake = Snake()
        wall = Wall(lvl)
        level = level_and_cnt(lvl)

    screen.fill((0, 0, 0))
    drawGrid()  

    snake.draw() 
    food.draw() 
    wall.draw()
    level.draw(cnt)

    pg.display.update()
    clock.tick(5)

