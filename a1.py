import time
import sys
from random import randrange as rand
import pygame, os
from a2 import *
from a3 import *
class Gameplay(Block, GAME_BOARD):
	def __init__(self):
		pygame.init()
		self.LEVEL_SCORES  =  [0, 40, 100, 300, 1200]
		pygame.key.set_repeat(250,25)
		m = rand(len(tetris_BLOCK_SHAPEs))
		self.SCORE = 0
		self.level = 1
		self.NUMBER_LINES = 0
		self.default_font  =   pygame.font.Font(
		pygame.font.get_default_font(), 12)	
		self.ROW_END = cell_size*c
		self.BACKGROUND_MATRIX = []
		for y in xrange(r):
			self.BACKGROUND_MATRIX.append([])
			for x in xrange(c):
				self.BACKGROUND_MATRIX[y].append(8)					
		self.width = cell_size*(c+10)
		self.height = cell_size*r
		self.screen = pygame.display.set_mode((self.width, self.height))
		self.next_BLOCK  =  tetris_BLOCK_SHAPEs[m]
		self.GAME_END  =  False
		self.tempdelay  =  1000
		self.wallcount = 0
		self.init_game()
	def DRAW_BOARD(self):
		pygame.draw.line(self.screen,(65,155,95),(self.ROW_END+1, 5),(self.ROW_END+1, self.height-1))
		self.DRAW(self.BACKGROUND_MATRIX,(0,0))
		self.DRAW(self.GAME_BOARD,(0,0))
		self.DRAW(self.BLOCK,
		(self.BLOCK_x, self.BLOCK_y))	
	def checkRowful(self,cleared_r):
					c_r = 0
					while True:
						for i in xrange(len(self.GAME_BOARD[:-1])):
							if 0 not in self.GAME_BOARD[:-1][i]:
								self.GAME_BOARD  =  self.remove_row(
							  	self.GAME_BOARD, i)
								c_r +=  1
								break
						else:
							return c_r
	def select_piece(self):
		m = rand(len(tetris_BLOCK_SHAPEs))
		self.BLOCK = self.next_BLOCK[:]
		self.next_BLOCK = tetris_BLOCK_SHAPEs[m]
		self.BLOCK_x = int(c / 2 - len(self.BLOCK[0])/2)
		self.BLOCK_y = 0
		
		if self.checkPiecePos(self.GAME_BOARD,
		                   self.BLOCK,
		                   (self.BLOCK_x, self.BLOCK_y)):
			self.GAME_END  =  True
	def init_game(self):
		self.GAME_BOARD = self.create_GAME_BOARD()
		self.select_piece()		
		pygame.time.set_timer(pygame.USEREVENT+1, 1000)
	def remove_row(self,GAME_BOARD, row):
		del GAME_BOARD[row]
		return [[0 for i in xrange(c)]] + GAME_BOARD
	def show(self, msg, topleft,colors):
		x,y = topleft
		c1,c2,c3 = colors
		for line in msg.splitlines():
			self.screen.blit(
				self.default_font.render(
					line,
					False,
					(c1,c2,c3),
					(0,0,0)),
				(x,y))
			y += 14			
	def move(self,shift_x,flag):
		if flag == 'L':
			self.GO_LEFT((-1)*(shift_x))
		elif flag == 0 :
			self.GO_RIGHT(shift_x)
	def quit(self):
		pygame.display.update()
		sys.exit()		
	def start_game(self):
		if self.GAME_END:
			self.init_game()
			self.GAME_END  =  False
	def SHOW_SCOREBOARD(self):
		pygame.draw.line(self.screen,(65,55,95),(self.ROW_END+10, cell_size*18-80),(self.ROW_END+200,cell_size*18-80))
		self.show("SCOREBOARD",(self.ROW_END+cell_size*3, (cell_size*18)-70),(255,0,0))
		self.show("SCORE: %d " % (self.SCORE),(self.ROW_END+cell_size, (cell_size*18-40)),(65,155,195))
		self.show("Level: %d " %(self.level),(self.ROW_END+cell_size, (cell_size*18-10)),(65,155,195))
		self.show("NUMBER_LINES: %d "%(self.NUMBER_LINES),(self.ROW_END+cell_size, (cell_size*18)+20),(65,155,195))
		pygame.draw.line(self.screen,(65,55,95),(self.ROW_END+10, cell_size*18+50),(self.ROW_END+200,cell_size*18+50))
		self.show("CONTROLS",(self.ROW_END+cell_size*3, (cell_size*18)+60),(255,0,0))
		self.show("S TO ROTATE",(self.ROW_END+cell_size, (cell_size*18)+90),(65,155,195))
		self.show("A TO MOVE LEFT",(self.ROW_END+cell_size, (cell_size*18)+110),(65,155,195))
		self.show("D TO MOVE RIGHT",(self.ROW_END+cell_size, (cell_size*18)+130),(65,155,195))
		self.show("X TO MOVE DOWN",(self.ROW_END+cell_size, (cell_size*18)+150),(65,155,195))
		self.show("SPACE FOR QUICK FALL",(self.ROW_END+cell_size, (cell_size*18)+170),(65,155,195))
		self.show("Q TO QUIT GAME",(self.ROW_END+cell_size, (cell_size*18)+190),(65,155,195))

	def LEVEL_INCREMENT(self):
		self.level += 1
		self.wallcount += 1
		m = rand(len(wall_BLOCK_SHAPEs))
		wall_type = wall_BLOCK_SHAPEs[m]
		wall_x = rand(25)+2
		wall_y = rand(25)+2
		while True:
			m = rand(len(wall_BLOCK_SHAPEs))
			wall_type = wall_BLOCK_SHAPEs[m]
			wall_x = rand(25)+2
			wall_y = rand(25)+2			
			if self.checkPiecePos(self.GAME_BOARD,wall_type,(wall_x, wall_y)):
				m = rand(len(wall_BLOCK_SHAPEs))
				wall_type = wall_BLOCK_SHAPEs[m]
				wall_x = rand(23) + 5
				wall_y = rand(23) + 5
			else:
				self.GAME_BOARD = self.fillPiecepos(self.GAME_BOARD,wall_type,(wall_x,wall_y))
				break
		self.tempdelay = 1000 - 60*(self.level-1)
		if self.tempdelay <= 200 :
			self.tempdelay = 200
		pygame.time.set_timer(pygame.USEREVENT+1,self.tempdelay)
		ret = []
		ret.append(wall_x)
		ret.append(wall_y)
		ret.append(wall_type)
		return ret
	def UpdateSCOREs(self, n):		
		self.SCORE += self.LEVEL_SCORES[n]*(self.level+1)
		self.NUMBER_LINES += n
		if self.NUMBER_LINES >= (self.level)*5:
			self.LEVEL_INCREMENT()
	def GAME_END_DISPLAY(self):
		pygame.draw.line(self.screen,(65,55,95),(self.ROW_END+10, cell_size*18-180),(self.ROW_END+200,cell_size*18-180))
		self.show("""SORRY GameOver!\n""",(self.ROW_END+10,cell_size*18-160),(255,0,0))
		self.show("""YOU SCORED: %d\n"""% self.SCORE,(self.ROW_END+10,cell_size*18-140),(255,0,0))
		self.show("""PRESS ENTER TO RESTART GAME""",(self.ROW_END+10,cell_size*18-120),(255,0,0))																				
	def DRAW_NEXT_BLOCK(self):
		self.DRAW(self.next_BLOCK,(c+3,4))
		self.show("Next Block :", (self.ROW_END+(cell_size*2),10),(255,0,0))		
	def START_GAME(self):
		KeyBindings  =  {
			'q':self.quit,'a':lambda:self.move(1,'L'),'d':lambda:self.move(1,0),'x':lambda:self.FALL(),'s':self.ROTATE,
			'RETURN':self.start_game,'SPACE':self.FAST_DROP,'i':self.LEVEL_INCREMENT}	
		self.GAME_END  =  False		
		ticking  =  pygame.time.Clock()
		while 1:
			if not self.GAME_END:
				self.screen.fill((8,8,8))
			if self.GAME_END:
				self.GAME_END_DISPLAY()
			else:
				self.DRAW_BOARD()				
				self.DRAW_NEXT_BLOCK()
				self.SHOW_SCOREBOARD()
			pygame.display.update()			
			for GAME_EVENT in pygame.event.get():
				if GAME_EVENT.type  ==  pygame.KEYDOWN:
					for key in KeyBindings:
						if GAME_EVENT.key  ==  eval("pygame.K_"
						+key):
							KeyBindings[key]()
					ticking.tick(25)				
				elif GAME_EVENT.type  ==  pygame.QUIT:
					self.quit()
				elif GAME_EVENT.type  ==  pygame.USEREVENT+1:
					self.FALL()				
App  =  Gameplay()
App.START_GAME()

	