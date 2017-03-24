import time
import sys,os
from random import randrange as rand
import pygame
c  =   32
r  =   30
tetris_BLOCK_SHAPEs  =  []
tetris_BLOCK_SHAPEs.append([[2, 2, 2],[0, 2, 0]])
tetris_BLOCK_SHAPEs.append([[7, 7, 0],[0, 7, 7]])
tetris_BLOCK_SHAPEs.append([[0, 0, 6],[6, 6, 6]])
tetris_BLOCK_SHAPEs.append([[4, 0, 0],[4, 4, 4]])
tetris_BLOCK_SHAPEs.append([[5, 5, 5, 5]])
tetris_BLOCK_SHAPEs.append([[3, 3],[3, 3]])
palette = []
palette.append((255,   255,  105 ))
palette.append((155, 85,  83))
palette.append((255, 140, 150 ))
palette.append((190,  120, 102 ))
palette.append((146, 202, 73 ))
palette.append((46, 200, 115))
palette.append((120, 188, 235))
palette.append((150, 141, 218 ))
palette.append((55,  55,  155))
palette.append((0,0,0))
wall_BLOCK_SHAPEs = []
wall_BLOCK_SHAPEs.append([[9,9,9],[9,9,9],[9,9,9]])
wall_BLOCK_SHAPEs.append([[9,9,0,0],[0,9,9,0],[0,0,9,9]])
wall_BLOCK_SHAPEs.append([[9,9],[9,9],[9,9],[9,9]])
wall_BLOCK_SHAPEs.append([[0,0,9,9],[0,9,9,0],[9,9,0,0]])
wall_BLOCK_SHAPEs.append([[9, 9, 9, 9]])
wall_BLOCK_SHAPEs.append([[9, 9],[9, 9]])
class GAME_BOARD():
        def fillPiecepos(self,matrix1, matrix2, matrix2_off):
                d_x, d_y  = matrix2_off
                for i in range(len(matrix2)):
                        for j in range(len(matrix2[i])):
                                matrix1[i+d_y-1][j+d_x] += matrix2[i][j]
                return matrix1
        def create_GAME_BOARD(self):
                GAME_BOARD = []
                for x in range(r):
                    GAME_BOARD.append([])
                    for y in range(c):
                        GAME_BOARD[x].append(0)
                GAME_BOARD.append([])
                for x in range(c):
                    GAME_BOARD[r].append(1)
                return GAME_BOARD
        def checkPiecePos(self,GAME_BOARD,BLOCK_SHAPE,offset):
                d_x, d_y  =  offset
                for i in xrange(len(BLOCK_SHAPE)):
                        for j in xrange(len(BLOCK_SHAPE[i])):
                                if i<r and j<c and i+d_y<r and j+d_x<c and j+d_x >= 0 and i+d_y >= 0:
                                    if BLOCK_SHAPE[i][j] != 0 and GAME_BOARD[i+d_y][j+d_x] != 0:
                                            return True
                                else:            
                                    return True
                return False

