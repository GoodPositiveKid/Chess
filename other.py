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