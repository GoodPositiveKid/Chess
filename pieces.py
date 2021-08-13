import pygame
from pygame.sprite import Sprite
from other import Spritesheet
class Piece(Sprite):
    """The base class for a chess piece"""
    def __init__(self, color, game, x,y, board):
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
            self.image = self.spritesheet.image(70,72,85,85)
        else:
            self.image = self.spritesheet.image(70,215,85,85)
class Queen(Piece):
    """Class for a Queen"""
    def __init__(self, color, game, x,y, board):
        super().__init__(color,game, x, y, board)
        if (color == "Black"):
            self.image = self.spritesheet.image(233,72,85,85)
        else:
            self.image = self.spritesheet.image(233,215,85,85)
class Rook(Piece):
    """Class for a Rook"""
    def __init__(self, color, game, x, y, board):
        super().__init__(color, game, x, y, board)
        if (color == "Black"):
            self.image = self.spritesheet.image(410,72,85,85)
        else:
            self.image = self.spritesheet.image(410,215,85,85)
class Bishop(Piece):
    """Class for a Bishop"""
    def __init__(self, color, game, x, y, board):
        super().__init__(color, game, x, y, board)
        if (color == "Black"):
            self.image = self.spritesheet.image(575,72,85,85)
        else:
            self.image = self.spritesheet.image(575,215,85,85)
class Knight(Piece):
    """Class for a Knight"""
    def __init__(self, color, game, x, y, board):
        super().__init__(color, game, x, y, board)
        if (color == "Black"):
            self.image = self.spritesheet.image(740,72,85,85)
        else:
            self.image = self.spritesheet.image(740,215,85,85)
class Pawn(Piece):
    """Class for a Pawn"""
    def __init__(self, color, game, x, y, board):
        super().__init__(color, game, x, y, board)
        if (color == "Black"):
            self.image = self.spritesheet.image(910,72,85,85)
        else:
            self.image = self.spritesheet.image(910,215,85,85)