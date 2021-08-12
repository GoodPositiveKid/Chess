import sys ,pygame,os
from pygame.sprite import Sprite
class Board:
    """Draws all the squares on the board"""
    def __init__(self,game):
        self.game = game
        self.squares = pygame.sprite.Group()
        self.coordinates = []
    def drawboard(self):
        for j in range(0,8):
            self.coordinates.append([])
            for i in range(0,8):
                temp = Square(self.game,self.game.width *(1/8) + self.game.width*(3/32)*i,self.game.width *(1/8) + self.game.width*(3/32)*j,i,j)
                self.squares.add(temp)
                self.coordinates[j].append([temp.rect.centerx,temp.rect.centery])
    def blitboard(self):
        self.squares.update()
        for i in self.squares.sprites():
                i.blitme()
    def getxy(self,x,y):
        return self.coordinates[y-1][x-1]
class Square(Sprite):
    """The class for a square"""
    def __init__(self,game,x,y,gridx,gridy):
        self.gridx = gridx
        self.gridy = gridy
        self.x = x
        self.y = y
        self.color = (255,255,255)
        if ((self.gridx+self.gridy*9)%2==1):
            self.color = (0,0,0)
        self.game = game
        self.rect = pygame.Rect(x,y,10,10)
    def blitme(self):
        self.rect = pygame.Rect(self.x,self.y,self.game.width*(3/32),self.game.width*(3/32))
        pygame.draw.rect(self.game.screen,self.color,self.rect)