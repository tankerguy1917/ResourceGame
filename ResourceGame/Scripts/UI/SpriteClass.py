###### SPRITE CLASS FILE ######

#### Imports ####
import pygame

#### Class Sprite ####
class Sprite:
	def __init__(self, img, x, y, w, h):
		self.sprite = pygame.Surface((w, h))
		self.sprite.blit(img, (-x, -y))
		self.sprite.set_colorkey((0, 0, 0))