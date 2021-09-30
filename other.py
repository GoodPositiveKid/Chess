import pygame
import pathlib

class Spritesheet:
    def __init__(self,filename):
        self.path = str(pathlib.Path(__file__).parent.absolute())
        self.sheet = pygame.image.load(self.path + '/' + filename).convert()
    def image(self,x,y,width,height):
        image = pygame.Surface([width, height]).convert()
        image.blit(self.sheet, (0, 0), (x, y, width, height))
        image.set_colorkey((255,255,255))
        return image
class Move:
    def __init__(self,piece,x,y):
        self.piece = piece
        self.to_x = x
        self.to_y = y
        self.board = piece.board
    def move(self):
        self.board.getsquare(self.piece.gridx,self.piece.gridy).piece = None
        self.piece.gridx = self.to_x
        self.piece.gridy = self.to_y
        self.board.getsquare(self.piece.gridx,self.piece.gridy).piece = self.piece