import pygame
from pygame.sprite import Sprite
from other import Spritesheet
class Piece(Sprite):
    """The base class for a chess piece"""
    def __init__(self,game,x,y,board,color):
        self.gridx = x
        self.gridy = y
        self.board = board
        self.game = game
        self.image = None
        self.spritesheet = Spritesheet("images/chess_pieces.bmp")
        self.color = color
    def blitme(self):
        xy = self.board.getxy(self.gridx,self.gridy)
        self.game.screen.blit(self.image,pygame.Rect(xy[0],xy[1],50,50))
class King(Piece):
    """Class for a king"""
    def __init__(self,color,game,x,y,board):
        super().__init__(game, x, y, board, color)
        if (color == "Black"):
            self.image = self.spritesheet.image(70,70,85,85,(255,255,255))
        else:
            self.image = self.spritesheet.image(70,200,85,100,(255,255,255))