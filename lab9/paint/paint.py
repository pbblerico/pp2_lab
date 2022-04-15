import pygame as pg

pg.init()

class tools(pg.sprite.Sprite): #visually defines the instrument panel
    def __init__(self, pic, position):
        super().__init__()
        self.pic = pg.image.load(f'tools/{pic}')
        self.pic = pg.transform.scale(self.pic, (30, 30))
        self.rect = self.pic.get_rect(center = position)
    def draw(self):
        screen.blit(self.pic, self.rect)

class pallete(pg.sprite.Sprite): #visually creates the pallete 
    def __init__(self, color, position):
        super().__init__()
        self.color = color
        self.position = position
        self.unit = pg.Surface((30, 30))
        self.rect = self.unit.get_rect(center = position)
    def draw(self):
        self.unit.fill(self.color)
        screen.blit(self.unit, self.rect)

def constant_elements(): #the elements that are constantly should be shown on the screen
    pg.draw.rect(screen, (128, 128, 220), pg.Rect(0, 0, 800, 50))
    for color in Colors:
        color.draw()
    for tool in Tools:
        tool.draw()

def calculateRect(x1, y1, x2, y2): #defines the rectangles
    r = pg.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))
    pg.draw.rect(screen, current_color, pg.Rect(r), capacity)

def calculateSquare(x1, y1, x2, y2): #defines the square
    r = pg.Rect(min(x1, x2), min(y1, y2), max(abs(x1 - x2), abs(y1 - y2)), max(abs(x1 - x2), abs(y1 - y2)))
    pg.draw.rect(screen, current_color, pg.Rect(r), capacity)

def calculatedCircle(x1, y1, x2, y2): #defines the circle
    r = max(abs(x2 - x1), abs(y2 - y1))
    pg.draw.circle(screen, current_color, (x1, y1), r, capacity)

def calculate_eqTriangle(x1, y1, x2, y2): #defines the equilateral triangle
    r = max(abs(y2 - y1), abs(x2 - x1))
    pg.draw.polygon(screen, current_color, ((x1, y1), (x1 - r, y1 + r), (x1 + r, y1 + r)), capacity)

def calculate_rTriangle(x1, y1, x2, y2): #defines the right triangle
    r = max(abs(y2 - y1), abs(x2 - x1))
    pg.draw.polygon(screen, current_color, ((x1, y1), (x1, y1 - r), (x1 + r, y1)), capacity)

def calculate_rhombus(x1, y1, x2, y2): #defines the rhombus
    r = max(abs(y2 - y1), abs(x2 - x1))
    pg.draw.polygon(screen, current_color, ((x1, y1), (x1 + r//2, y1 + r//2), (x1, y1 + r), (x1 - r//2, y1 + r//2)), capacity)

#changes the size of the tools
def the_size(i):
    global capacity
    if i.key == pg.K_1:
        capacity = 1
    if i.key == pg.K_2:
        capacity = 5
    if i.key == pg.K_3:
        capacity = 10
    if i.key == pg.K_4:
        capacity = 15
    if i.key == pg.K_5:
        capacity = 20
    if i.key == pg.K_0:
        capacity = 0

#makes the bool part of all figure instruments False in order to escape using several tools at the same time 
def figure_tools_setting():
    global FigureMode 
    baseLayer.blit(screen, (0, 0))
    FigureMode = True
    for i in state:
        state[i] = False

width, height = 800, 600
pg.display.set_caption('Paint')
screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()

#creating the palette of colors with list c and class palette 
color_and_position = [[(255, 0, 0), (20, 20)], [(255, 165, 0), (55, 20)], [(255, 255, 0), (90, 20)], [(0, 255, 0), (125, 20)], [(135, 206, 235), (160, 20)], 
    [(0, 0, 255), (195, 20)], [(255, 0, 255), (230, 20)], [(255, 255, 255), (265, 20)], [(150, 75, 0), (300, 20)], [(0, 0, 0), (335, 20)]]
Colors = pg.sprite.Group()
for i in color_and_position:
    temp = pallete(i[0], i[1])
    Colors.add(temp)

#creating the sprite group of instruments for future work panel
items = [['eraser.png', (495, 20)], ['pen.png', (530, 20)], ['rect.png', (565, 20)], ['circle.png', (600, 20)], ['square.png', (635, 20)],
        ['right_triangle.png', (670, 20)], ['eq_triangle.png', (705, 20)], ['rhombus.png', (740, 20)]]
Tools = pg.sprite.Group()
for i in items:
    temp = tools(i[0], i[1])
    Tools.add(temp)

capacity = 1
baseLayer = pg.Surface((width, height))
screen.fill((255, 255, 255))
baseLayer.fill((255, 255, 255))

prevX = currentX = 0
prevY = currentY = 0
current_color = color_and_position[-1][0]

run,  DrawMode = True, False
pen, FigureMode = True, False
state = {'rect': False, 'circle': False, 'square': False, 'right_triangle': False, 'eq_triangle': False, 'rhombus': False}
while run:
    j = 0
    for i in pg.event.get():
        if i.type == pg.QUIT:
            run = not run
        if i.type == pg.KEYDOWN:
            if i.key == pg.K_c:
                screen.fill((255, 255, 255)) #completely clears the layer
            the_size(i)
        if i.type == pg.MOUSEBUTTONDOWN:
                DrawMode = True
                if FigureMode: 
                    prevX = i.pos[0]
                    prevY = i.pos[1]
        if i.type == pg.MOUSEBUTTONUP:
            DrawMode = False
            if FigureMode: baseLayer.blit(screen, (0, 0))
        if i.type == pg.MOUSEMOTION: #detects the current position
            currentX = i.pos[0]
            currentY = i.pos[1]

    #draws the pallete and changes the color of the pen when it's picked by a mouseclick
    for color in Colors:
        point = pg.mouse.get_pos()
        if color.rect.collidepoint(point) and pg.MOUSEBUTTONDOWN and pen:
            current_color = color_and_position[j][0]
        j += 1

    #changes the pen to eraser or figure tools by a click detection
    k = 0
    for tool in Tools:
        point = pg.mouse.get_pos()
        if tool.rect.collidepoint(point) and pg.MOUSEBUTTONDOWN: #the tool is picked only if it's clicked in it's area
            if 'eraser' in items[k][0]:
                FigureMode = pen = False #the eraser can't have figure form 
                current_color = (255, 255, 255)
            elif 'pen' in items[k][0]:
                FigureMode, pen = False, True
                current_color = (0, 0, 0)
            elif 'rect' in items[k][0]:
                figure_tools_setting()
                state['rect'] = True
            elif 'circle' in items[k][0]:
                figure_tools_setting()
                state['circle'] = True
            elif 'square' in items[k][0]:
                figure_tools_setting()
                state['square'] = True
            elif 'right_triangle' in items[k][0]:
                figure_tools_setting()
                state['right_triangle'] = True
            elif 'eq_triangle' in items[k][0]:
                figure_tools_setting()
                state['eq_triangle'] = True
            elif 'rhombus' in items[k][0]:
                figure_tools_setting()
                state['rhombus'] = True
        k += 1

    #Draws with figure tools 
    if DrawMode and FigureMode:
        if not pen: #turns on the pen mode automatically if previously eraser was used (initial color: black)
            pen = not pen
            current_color = (0, 0, 0)
        screen.blit(baseLayer, (0, 0))
        #draws the figure if it's mode is on
        if state['circle']: calculatedCircle(prevX, prevY, currentX, currentY)
        if state['rect']: calculateRect(prevX, prevY, currentX, currentY)
        if state['square']: calculateSquare(prevX, prevY, currentX, currentY)
        if state['right_triangle']: calculate_rTriangle(prevX, prevY, currentX, currentY)
        if state['eq_triangle']: calculate_eqTriangle(prevX, prevY, currentX, currentY)
        if state['rhombus']: calculate_rhombus(prevX, prevY, currentX, currentY)

    #Draws with pen or eraser
    if not FigureMode: #no figure tools
        if DrawMode:
            if capacity == 0: capacity = 25 #since for the line 0 can't draw a line I made it 
            pg.draw.line(screen, current_color, (prevX, prevY), (currentX, currentY), capacity)
        prevX = currentX
        prevY = currentY
    constant_elements() #constantly blits constant elements like color panel and some instruments
    clock.tick(60)
    pg.display.update()