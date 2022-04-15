import pygame as pg
from random import randint 
import time

pg.init()

#opening 
def start_of_the_game():
    text = font1.render('Press SPACE to start!', True, (255, 165, 0))
    name_1 = font2.render('STREET', True, (255, 165, 0))
    name_2 = font2.render('RACER', True, (255, 165, 0))
    pic = pg.transform.scale(pg.image.load('pictures/opening.png'), (256, 256))

    screen.blit(pic, (70, 100))
    screen.blit(text, (40, 550))
    screen.blit(name_1, (100, 50))
    screen.blit(name_2, (115, 360))

    pg.mixer.music.load('sounds/theme_song.mp3')
    pg.mixer.music.play(-1)

#shows up when player collides with enemy car and the game closes
def game_over():
    explosion = pg.transform.scale(pg.image.load('pictures/explosion.png'), (250, 250))
    screen.fill((0, 0, 0))
    
    text = font2.render('GAME OVER!', True, (255, 165, 0))
    text_2 = font.render('Maybe next time...', True, (255, 165, 0))
    screen.blit(explosion, (75, 90)) 
    screen.blit(text, (40, 50)) 
    screen.blit(text_2, (130, 310)) 
    pg.draw.line(screen, (255, 165, 0), (0, 340), (width, 340), 5)

    #sound of explosion
    pg.mixer.music.load('sounds/explosion_sound.mp3')
    pg.mixer.music.play(0)

#counts the current score and updates it
class score:
    def __init__(self):
        self.point = 0 
        self.score_add = [1, 3, 5]

    def count(self):
        global cnt
        cnt += 1
        self.point += self.score_add[Coin.current_image]

    def draw(self):
        text = font.render(f'Score: {self.point}', True, (0, 0, 0))
        screen.blit(text, (320, 10))

    def draw_when_lose(self):
        text = font1.render(f'Score: {self.point}', True, (255, 165, 0))
        screen.blit(text, (120, 350))

#classes for the player, enemies and coins
class player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.step = 5
        self.image = pg.image.load('pictures/Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (200, 450)

    def update(self): 
        pressed = pg.key.get_pressed()
        if self.rect.left > 0:
            if pressed[pg.K_LEFT]:
                self.rect.move_ip(-self.step, 0)
        if self.rect.right < width:
            if pressed[pg.K_RIGHT]:
                self.rect.move_ip(self.step, 0)

    def draw(self):
        screen.blit(self.image, self.rect)

class enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.step = 10
        self.image = pg.image.load('pictures/Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (randint(30, 370), 50)

    def update(self):
        self.rect.move_ip(0, self.step)
        if self.rect.bottom > height:
            self.rect.center = (randint(30, 370), 50)

    def draw(self):
        screen.blit(self.image, self.rect)

#initializing the coin and moving it along the game
class coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.step = 5
        self.coins = ['coin_red.png', 'coin.png', 'coin_blue.png']
        rand = randint(0, 2) #randomly takes one of the coins
        self.current_image = rand
        self.image = pg.transform.scale(pg.image.load(f'pictures/{self.coins[rand]}'), (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (randint(25, 375), 20)
    
    def update(self):
        self.rect.move_ip(0, self.step)
        if self.rect.bottom > height:
            self.rect.center = (randint(25, 375), 20)

    def collision(self):
        rand = randint(0, 2)
        self.current_image = rand
        self.image = pg.transform.scale(pg.image.load(f'pictures/{self.coins[rand]}'), (40, 40))
        self.rect.center = (randint(25, 375), 20)

    def draw(self):
        screen.blit(self.image, self.rect)


pg.display.set_caption('Street Racer')
width, height = 400, 600
screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()
fpc, n = 50, 10
cnt = 0

font1 = pg.font.SysFont('Verdana', 30)
font2 = pg.font.SysFont('Verdana', 50)
font = pg.font.SysFont('Verdana', 15)
road = pg.image.load('pictures/AnimatedStreet.png')

run, start = True, False

#main objectss
Player = player()
Enemy_1 = enemy()
Coin = coin()
Score = score()

#combining all classes into one to update the progress easier
sprite_group = pg.sprite.Group()
enemies = pg.sprite.Group()
money = pg.sprite.Group()

money.add(Coin)
enemies.add(Enemy_1)
sprite_group.add(Coin)
sprite_group.add(Enemy_1)
sprite_group.add(Player)

while run:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            run = not run
            
    #the window that appears before the start
    while not start:
        start_of_the_game()
        for i in pg.event.get():
            if i.type == pg.KEYDOWN and i.key == pg.K_SPACE:
                start = not start
            if i.type == pg.QUIT:
                run = not run
                start = not start
        pg.display.update()
    
    screen.blit(road, (0, 0))

    #updates all the sprites
    for progress in sprite_group:
        progress.update()
        progress.draw()

    #closes the game when player loses
    if pg.sprite.spritecollideany(Player, enemies):
        game_over()
        Score.draw_when_lose()
        pg.display.update()
        time.sleep(3)
        run = not run

    #updates the score counter when player gets the coin
    if pg.sprite.spritecollideany(Player, money):
        Score.count()
        Coin.collision()

    if cnt > n: #increases the speed of the game when cnt(number of picked coins) is more than n 
        fpc += 0.5
        n += 10  #update our border  

    Score.draw() #draws the current score
    clock.tick(fpc)
    pg.display.update()

