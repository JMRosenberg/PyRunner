import sys, pygame
from tile import Tile
from levels import level1 as l1
pygame.init()

#screen and tile sizing
tileEdge = 40
tilesHigh = 16
tilesWide = 28
size = width, height = tilesWide*tileEdge, tilesHigh*tileEdge

screen = pygame.display.set_mode(size)
level = []

#load images
tiles = [None,
    pygame.image.load("resources/grass.png"),
    pygame.image.load("resources/stone.png"),
    pygame.image.load("resources/glue.png"),
    pygame.image.load("resources/bomb.png"),
    pygame.image.load("resources/ladder.png"),
    pygame.image.load("resources/monk.png"),
    pygame.image.load("resources/gold.png"),
    pygame.image.load("resources/door.png"),
    pygame.image.load("resources/player1.png")]

bg = pygame.image.load("resources/bg1.png")

#cleaner way to populate the level map
for y in range(0, tilesHigh):
    row = []
    for x in range(0, tilesWide):
        row.append(Tile(tiles[l1[y][x]]))
    level.append(row)

#main loop
while 1:
    #check for buttons, clicks, etc.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #draw the background first
    screen.blit(bg, (0,0))

    #then each of the tiles
    for y in range(0, tilesHigh):
        for x in range(0, tilesWide):
            if not level[y][x].image == None:
                screen.blit(level[y][x].image, (x*tileEdge, y*tileEdge))

    pygame.display.flip()
