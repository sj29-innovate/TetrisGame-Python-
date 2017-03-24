import time
import os
import sys
from random import randrange as rand
import pygame
from a2 import *
cell_size = 18;
class Block():
        def DO_ROTATE(self,BLOCK_SHAPE):
                temp = []
                t = len(BLOCK_SHAPE[0])
                t1 = len(BLOCK_SHAPE)
                for i in xrange(t):
                    temp.append([])
                    for j in xrange(t1):
                        temp[i].append(BLOCK_SHAPE[j][t-i-1])
                return temp
        def ROTATE(self):
                if not self.GAME_END:
                        temp = self.DO_ROTATE(self.BLOCK)
                        if not self.checkPiecePos(self.GAME_BOARD,
                                               temp,
                                               (self.BLOCK_x, self.BLOCK_y)):
                                self.BLOCK  =  temp
        def GO_LEFT(self,shift_x):
             if not self.GAME_END:
                        temp = len(self.BLOCK[0])
                        new_x = self.BLOCK_x
                        new_x += shift_x
                        if new_x + temp>c:
                            new_x = c 
                            new_x -= temp
                        if not new_x >= 0:
                            new_x =  0
                        if not self.checkPiecePos(self.GAME_BOARD, self.BLOCK,(new_x, self.BLOCK_y)):
                            self.BLOCK_x  =  new_x
        def GO_RIGHT(self,shift_x):
                if not self.GAME_END:
                        temp = len(self.BLOCK[0])
                        new_x = self.BLOCK_x
                        new_x += shift_x
                        if new_x + temp>c:
                            new_x = c 
                            new_x -= temp
                        if not new_x >= 0:
                            new_x =  0
                        if not self.checkPiecePos(self.GAME_BOARD,self.BLOCK,(new_x, self.BLOCK_y)):
                            self.BLOCK_x  =  new_x
        def DRAW(self, matrix, offset):
                off_x, off_y   =  offset
                temp1 = len(matrix)
                for y in range(temp1):
                        temp2 = len(matrix[y])
                        for x in range(temp2):
                                if matrix[y][x] != 0:
                                        matrix[y][x] = matrix[y][x]%10
                                        t1 = palette[matrix[y][x]]
                                        t2 = (off_x + x) * cell_size
                                        t3 = (off_y + y) * cell_size
                                        pygame.draw.rect(self.screen,t1,pygame.Rect(t2,t3,cell_size,cell_size),0)
        def FALL(self):
                if not self.GAME_END:
                        self.BLOCK_y +=  1
                        if self.checkPiecePos(self.GAME_BOARD,self.BLOCK,(self.BLOCK_x, self.BLOCK_y)):
                                self.GAME_BOARD  =  self.fillPiecepos(self.GAME_BOARD,self.BLOCK,(self.BLOCK_x, self.BLOCK_y))
                                self.select_piece()
                                cleared_r = self.checkRowful(0)
                                self.UpdateSCOREs(cleared_r)
                                return True
                return False
        def FAST_DROP(self):
                if not self.GAME_END:
                    while True:
                        if self.FALL() :
                            break;     

