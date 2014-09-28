tileEdge = 40
tilesHigh = 16
tilesWide = 28

class Player:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.speed = 5

    def move(self, direction, level):
        if direction == "Right":
            self.x = self.x + self.speed
        if direction == "Left":
            self.x = self.x - self.speed
#        if direction == "None":
#            if level[self.y/tileEdge-1][self.x/tileEdge] != 
