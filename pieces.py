import pygame
from pygame.sprite import Sprite
from other import Spritesheet,Move
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
        self.board.getsquare(self.gridx,self.gridy).piece = self
        self.selected = False
        self.moves = []
    def blitme(self):
        xy = self.board.getxy(self.gridx,self.gridy)
        self.game.screen.blit(self.image,pygame.Rect(xy[0],xy[1],50,50))
    def addmove(self,addx,addy,typeof="both",continues = False):
        if (self.gridx+addx <= 0 or self.gridx + addx >= 9) or (self.gridy+addy <= 0 or self.gridy + addy >= 9):
            return
        thepiece = self.board.getsquare(self.gridx+addx,self.gridy + addy).piece
        if (typeof=="move"and thepiece == None):
            self.moves.append(Move(self,self.gridx+addx,self.gridy+addy))
        if (typeof=="capture"and thepiece != None):
            if thepiece.color != thepiece.color:
                self.moves.append(Move(self,self.gridx+addx,self.gridy+addy))
        else:
            if (thepiece == None or thepiece.color != self.color):
                self.moves.append(Move(self,self.gridx+addx,self.gridy+addy))
        if (continues and not typeof == "capture" and not (typeof == "both" and thepiece != None and thepiece.color != self.color)):
            i = 2
            while 1:
                if (((self.gridx + i*addx) > 8 or (self.gridx + i*addx) < 1) or 
                (self.gridy + i*addy) > 8 or (self.gridy + i * addy) < 1):
                    break
                thepiece = self.board.getsquare(self.gridx + i*addx, self.gridy + i*addy).piece
                if (typeof == "both" and thepiece != None and thepiece.color != self.color):
                    self.moves.append(Move(self,self.gridx+i*addx,self.gridy + i*addy))
                    break
                if (typeof == "both" and thepiece != None and thepiece.color == self.color):
                    break
                if (typeof == "move" and thepiece != None):
                    break
                self.moves.append(Move(self,self.gridx + i*addx, self.gridy + i*addy))
                i += 1
    def addmoves(self,list):
        for i in list:
            if (len(i) == 3):
                self.addmove(i[0],i[1],i[2])
            elif (len(i) == 4):
                self.addmove(i[0],i[1],i[2],i[3])
            else:
                self.addmove(i[0],i[1])
    def light(self):
        for i in self.moves:
            i.light()
class King(Piece):
    """Class for a king"""
    def __init__(self,color,game,x,y,board):
        super().__init__(color,game, x, y, board)
        if (color == "Black"):
            self.image = self.spritesheet.image(70,72,85,85)
        else:
            self.image = self.spritesheet.image(70,215,85,85)
    def makemoves(self):
        self.addmoves([[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0]])
        return self.moves
class Queen(Piece):
    """Class for a Queen"""
    def __init__(self, color, game, x,y, board):
        super().__init__(color,game, x, y, board)
        if (color == "Black"):
            self.image = self.spritesheet.image(233,72,85,85)
        else:
            self.image = self.spritesheet.image(233,215,85,85)
    def makemoves(self):
        self.addmoves([[1,0,"both",True],[1,-1,"both",True],
        [0,-1,"both",True],[-1,-1,"both",True],[-1,0,"both",True],
        [-1,1,"both",True],[0,1,"both",True],[1,1,"both",True]])
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