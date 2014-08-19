import sys, pygame
from tile import Tile
from levels import level1 as l1
pygame.init()

tileEdge = 40 # pixels for each tile
tilesHigh = 16
tilesWide = 28
size = width, height = tilesWide*tileEdge, tilesHigh*tileEdge

screen = pygame.display.set_mode(size)
level = []
grass = pygame.image.load("resources/grass.png")
stone = pygame.image.load("resources/stone.png")
glue = pygame.image.load("resources/glue.png")
bg = pygame.image.load("resources/bg1.png")
player = pygame.image.load("resources/player1.png")
ladder = pygame.image.load("resources/ladder.png")
gold = pygame.image.load("resources/gold.png")
door = pygame.image.load("resources/door.png")
monk = pygame.image.load("resources/monk.png")
bomb = pygame.image.load("resources/bomb.png")

for y in range(0, tilesHigh):
    row = []
    for x in range(0, tilesWide):
        if l1[y][x] == 1:
            row.append(Tile(grass))
        elif l1[y][x] == 2:
            row.append(Tile(stone))
        elif l1[y][x] == 3:
            row.append(Tile(glue))
        elif l1[y][x] == 4:
            row.append(Tile(bomb))
        elif l1[y][x] == 5:
            row.append(Tile(ladder))
        elif l1[y][x] == 6:
            row.append(Tile(monk))
        elif l1[y][x] == 7:
            row.append(Tile(gold))
        elif l1[y][x] == 8:
            row.append(Tile(door))
        elif l1[y][x] == 9:
            row.append(Tile(player))
        else:
            row.append(Tile())
    level.append(row)

black = 0, 0, 0
blue = 0, 0, 255
screencolor = black

#ball = pygame.image.load("resources/stone.png")
#ballrect = ball.get_rect()
#ballrect = ballrect.move([100, 100])
#screen.fill(screencolor)
#b = screen.blit(ball, ballrect)
#pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            #if b.collidepoint(pos):
                #if screencolor == black:
                    #screencolor = blue
                #else:
                    #screencolor = black

    screen.blit(bg, (0,0))

    for y in range(0, tilesHigh):
        for x in range(0, tilesWide):
            if not level[y][x].image == None:
                screen.blit(level[y][x].image, (x*tileEdge, y*tileEdge))

    pygame.display.flip()
