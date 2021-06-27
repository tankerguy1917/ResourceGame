###### GAME CLASS FILE ######

#### Imports ####
import pygame
from pygame.locals import *

#### Class Game ####
class Game:
	def __init__(self, x, y, img_size):
		self.screen = pygame.Surface((x, y))
		self.money = 100
		self.resource_list = []

		self.rect_list = []
		y_pos = 0
		for i in range(y // img_size):
			x_pos = 0
			for n in range(x // img_size):
				self.rect_list.append(pygame.Rect(x_pos * img_size, y_pos * img_size, img_size, img_size))
				x_pos += 1
			y_pos += 1