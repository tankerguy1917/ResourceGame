###### BUTTON CLASS FILE ######

#### Imports ####
import pygame
from pygame.locals import *

#### Button class ####
class Button:
	def __init__(self, img, x, y):
		self.img = img
		self.button = pygame.Rect(x, y, self.img.get_width(), self.img.get_height())

	def display(self, surf):
		surf.blit(self.img, (self.button[0], self.button[1]))		