import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object):
	rows = 0
	w = 0
	def __init__(self, start, dirx=1, diry=0, color=(255,0,0)):
		pass
	def move(self, dirx, diry):
		pass
	def draw(self, surface, eyes=False):
		pass


class snake(object):
	snk_body = []
	turns = {}
	def __int__(self, color, pos):
		self.color = color
		self.head = cube(pos)
		self.snk_body.append(self.head)
		self.dirx = 0 # direction - x
		self.diry = 0 # direction - y

	def move(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT():


	def reset(self, pos):
		pass
	def addCube(self):
		pass
	def draw(self, surface):
		pass

def drawGrid(w, rows, surface):
	size = w // rows

	x = 0
	y = 0
	for l in range(rows):
		x = x + size
		y = y + size

		pygame.draw.line(surface, (255,255, 255), (x,0), (x,w)) # horizontal lines of grid
		pygame.draw.line(surface, (255,255, 255), (0, y), (w,y)) #vertical lines of the grid
	

def redrawWindow(surface):
	global rows, width
	surface.fill((0, 0, 0))
	drawGrid(width, rows, surface)
	pygame.display.update()

def randomSnack(rows, items):
	pass

def message_box(subject, content):
	pass

def main():
	global width, height, rows
	width = 500
	height = 500
	rows = 20

	win = pygame.display.set_mode((width, height))

	# snk = snake((255, 0, 0), (10, 10))
	flag = True

	clock = pygame.time.Clock()

	while flag:
		pygame.time.delay(50) # adding delay to snake's move - high delay, slow snake -- low delay, fast snake
		clock.tick(10) # snake will move 10 blocks in every second

		redrawWindow(win)


# rows = 
# w =
# h = 

# cube.rows = rows
# cube.w = w

main()