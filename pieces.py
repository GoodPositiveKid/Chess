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
        self.square = self.board.getsquare(self.gridx,self.gridy)
        self.square.piece = self
        self.selected = False
        self.moves = []
        self.xy = self.board.getxy(self.gridx,self.gridy)
    def blitme(self):
        self.game.screen.blit(self.image,pygame.Rect(self.xy[0],self.xy[1],50,50))
    def addmove(self,addx,addy,typeof="both",continues = False):
        if (self.gridx+addx <= 0 or self.gridx + addx >= 9) or (self.gridy+addy <= 0 or self.gridy + addy >= 9):
            return
        thepiece = self.board.getsquare(self.gridx+addx,self.gridy + addy).piece
        if (typeof=="move"and thepiece == None):
            self.moves.append(Move(self,self.gridx+addx,self.gridy+addy))
        if (typeof == "both" and thepiece != None and thepiece.color == self.color):
            return
        if (typeof == "capture" and thepiece == None):
            return
        if (typeof=="capture" and thepiece != None):
            if thepiece.color != self.color:
                self.moves.append(Move(self,self.gridx+addx,self.gridy+addy))
        else:
            if (typeof == "both" and thepiece == None or typeof == "both" and thepiece.color != self.color):
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
                    return
                if (thepiece != None and thepiece.color == self.color):
                    break
                    return
                if (typeof == "move" and thepiece != None):
                    break
                    return
                self.moves.append(Move(self,self.gridx + i*addx, self.gridy + i*addy))
                i += 1
        return
    def addmoves(self,l):
        for i in l:
            if (len(i) == 3):
                self.addmove(i[0],i[1],typeof = i[2])
            elif (len(i) == 4):
                self.addmove(i[0],i[1],typeof = i[2],continues = i[3])
            else:
                self.addmove(i[0],i[1])
    def light(self,on):
        for i in self.moves:
            i.light(on)
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
        return self.moves
class Rook(Piece):
    """Class for a Rook"""
    def __init__(self, color, game, x, y, board):
        super().__init__(color, game, x, y, board)
        if (color == "Black"):
            self.image = self.spritesheet.image(410,72,85,85)
        else:
            self.image = self.spritesheet.image(410,215,85,85)
    def makemoves(self):
        self.addmoves([[0,1,"both",True],[0,-1,"both",True],
        [1,0,"both",True],[-1,0,"both",True]])
        return self.moves
class Bishop(Piece):
    """Class for a Bishop"""
    def __init__(self, color, game, x, y, board):
        super().__init__(color, game, x, y, board)
        if (color == "Black"):
            self.image = self.spritesheet.image(575,72,85,85)
        else:
            self.image = self.spritesheet.image(575,215,85,85)
    def makemoves(self):
        self.addmoves([
            [1,1,"both",True],[1,-1,"both",True],[-1,1,"both",True],[-1,-1,"both",True]
        ])
        return self.moves
class Knight(Piece):
    """Class for a Knight"""
    def __init__(self, color, game, x, y, board):
        super().__init__(color, game, x, y, board)
        if (color == "Black"):
            self.image = self.spritesheet.image(740,72,85,85)
        else:
            self.image = self.spritesheet.image(740,215,85,85)
    def makemoves(self):
        self.addmoves([
            [1,2],[-1,2],[-2,1],[-2,-1],[-1,-2],[1,-2],[2,-1],[2,1]
        ])
        return self.moves
class Pawn(Piece):
    """Class for a Pawn"""
    def __init__(self, color, game, x, y, board):
        super().__init__(color, game, x, y, board)
        if (color == "Black"):
            self.image = self.spritesheet.image(910,72,85,85)
        else:
            self.image = self.spritesheet.image(910,215,85,85)
    def makemoves(self):
        if (self.color == "White"):
            if (self.gridy == 2):
                self.addmove(0,2,typeof = "move")
            self.addmoves([[0,1,"move"],[-1,1,"capture"],[1,1,"capture"]])
        if (self.color == "Black"):
            if (self.gridy == 7):
                self.addmove(0,-2,typeof = "move")
            self.addmoves([[0,-1,"move"],[-1,-1,"capture"],[1,-1,"capture"]])
        return self.moves