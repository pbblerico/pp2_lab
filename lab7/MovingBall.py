import pygame as pg

pg.init()

clock = pg.time.Clock()

width, height = 600, 400
screen = pg.display.set_mode((width, height))
white = (255, 255, 255)
step = 20
x, y = 50, 50 
dx, dy = 0, 0
radius = 25
screen.fill(white)

run = True
while run:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            run = False

    key = pg.key.get_pressed()

    if key[pg.K_UP]: dx, dy = 0, -1
    if key[pg.K_DOWN]: dx, dy = 0, 1
    if key[pg.K_LEFT]: dx, dy = -1, 0
    if key[pg.K_RIGHT]: dx, dy = 1, 0
    
    if radius <= x + step * dx <= width - radius: x += step * dx
    elif x + step * dx < radius: x = radius
    else: x = width - radius

    if radius <= y + step * dy <= height - radius: y += step * dy
    elif y + step * dy < radius: y = radius
    else: y = height - radius

    screen.fill(white)
    pg.draw.circle(screen, (255, 0, 0), (x, y), radius)

    pg.display.flip()
    clock.tick(60)
