import sys ,pygame,os
from pygame.sprite import Sprite
from pieces import *
from other import Move
from math import sin, cos
class Board:
    """Draws all the squares on the board"""
    def __init__(self,game,x=0,y=0):
        self.x = x
        self.y = y
        self.game = game
        self.squares = pygame.sprite.Group()
        self.coordinates = []
        self.pieces = pygame.sprite.Group()
        self.selectedpiece = None
        self.move = "White"
        self.whitemoves = []
        self.blackmoves = []
        self.moves = []
    def drawboard(self,angle = 180):
        for j in range(0,8):
            self.coordinates.append([])
            for i in range(0,8):
                s_x = self.game.width *(1/8) + self.game.width*(3/32)*i
                s_y = self.game.width *(1/8) + self.game.width*(3/32)*j
                temp = Square(self.game,
                ((s_x+self.x)),
                ((s_y-self.y)),
                 i, j, self)
                self.squares.add(temp)
                self.coordinates[j].append(temp)
    def blitboard(self):
        self.squares.update()
        for i in self.squares.sprites():
                i.blitme()
    def getxy(self,x,y):
        square = self.coordinates[8-y][x-1]
        return [square.rect.x,square.rect.y,square.piece]
    def getsquare(self,x,y):
        return self.coordinates[8-y][x-1]
    def fen(self,fen):
        x = 1
        y = 9
        for row in fen.split('/'):
            y -= 1
            x =1
            for c in row:
                if c in '123456789':
                    x += int(c)
                else:
                    if c.isupper():
                        color = "White"
                    else:
                        color = "Black"
                    if c.lower() == "k":
                        piece = King(color,self.game,x,y,self)
                        self.pieces.add(piece)
                    elif c.lower() == "r":
                        piece = Rook(color,self.game,x,y,self)
                        self.pieces.add(piece)
                    elif c.lower() == "n":
                        piece = Knight(color,self.game,x,y,self)
                        self.pieces.add(piece)
                    elif c.lower() == "b":
                        piece = Bishop(color,self.game,x,y,self)
                        self.pieces.add(piece)
                    elif c.lower() == "q":
                        piece = Queen(color,self.game,x,y,self)
                        self.pieces.add(piece)
                    else:
                        piece = Pawn(color,self.game,x,y,self)
                        self.pieces.add(piece)
                    x+=1
    def allmoves(self):
        for piece in self.pieces.sprites():
            piece.makemoves()
            if (piece.color == "Black"):
                for move in piece.moves:
                    self.blackmoves.append(move)
                    self.moves.append(move)
            else:
                for moves in piece.moves:
                    self.whitemoves.append(move)
                    self.moves.append(move)
        return self.moves
class Square(Sprite):
    """The class for a square"""
    def __init__(self,game,x,y,gridx,gridy,board):
        self.board = board
        self.gridx = gridx
        self.gridy = gridy
        self.x = x
        self.y = y
        self.piece = None
        self.color = (255,255,255)
        self.selected = False
        if ((self.gridx+self.gridy*9)%2==1):
            self.color = (0,100,0)
        self.game = game
        self.rect = pygame.Rect(x,y,10,10)
    def blitme(self):
        self.rect = pygame.Rect(self.x,self.y,self.game.width*(3/32),self.game.width*(3/32))
        if (self.selected):
            pygame.draw.rect(self.game.screen,(139, 128, 0),self.rect)
        else:
            pygame.draw.rect(self.game.screen,self.color,self.rect)
        if (self.piece):
            self.piece.blitme()
    def isclicked(self):
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            return 2
        elif self.rect.collidepoint(pygame.mouse.get_pos()):
            return 1
        else:
            return 0