import sys ,pygame,os
import pathlib
from board import *
from other import *
from pieces import *
from pygame.sprite import Sprite
class Game:
    def __init__(self):
        self.board = Board(self)
        path = pathlib.Path(__file__).parent.absolute()
        pygame.init()
        info = pygame.display.Info()
        self.screen = pygame.display.set_mode((min(info.current_w,info.current_h),min((info.current_w,info.current_h))))
        self.width, self.height = self.screen.get_size()
        pygame.display.set_caption("Chess")
        self.board.drawboard()
        self.board.fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
        self.king = King("White",self,4,4,self.board)
        print(len(self.king.makemoves()))
    def run(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill([100,100,100])
            self.board.blitboard()
            pygame.display.flip()
if __name__ == '__main__':
    game = Game()
    game.run()