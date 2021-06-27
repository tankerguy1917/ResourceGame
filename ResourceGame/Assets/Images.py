###### IMAGE FILE ######

#### Imports ####
import pygame, sys
from pygame.locals import *
from ResourceGame.Scripts.UI.SpriteClass import Sprite

#### Ignore this ####
x = pygame.display.set_mode((0, 0))

#### UI elements ####
	## Buttons ##
buttons = pygame.image.load("ResourceGame/Assets/UI/Buttons.png").convert()
buttons.set_colorkey((0, 0, 0))

start_button_img1 = Sprite(buttons, 0, 0, 25, 7).sprite
cred_button_img1 = Sprite(buttons, 0, 7, 25, 7).sprite

collect_button_img = Sprite(buttons, 0, 14, 16, 14).sprite
sell_button_img = Sprite(buttons, 16, 14, 16, 14).sprite

	## Icons ##
icons = pygame.image.load("ResourceGame/Assets/UI/ResourceIcons.png").convert()
icons.set_colorkey((0, 0, 0))

wood_icon = Sprite(icons, 0, 0, 13, 13).sprite
stone_icon = Sprite(icons, 13, 0, 12, 12).sprite
iron_icon = Sprite(icons, 25, 0, 14, 12).sprite
gem_icon = Sprite(icons, 39, 0, 14, 14).sprite
money_icon = Sprite(icons, 53, 0, 11, 17).sprite

	## Resource collector icons ##
icons2 = pygame.image.load("ResourceGame/Assets/UI/ResourceCollectIcons.png").convert()
icons2.set_colorkey((0, 0, 0))

wood_col_icon = Sprite(icons2, 0, 0, 20, 20).sprite
stone_col_icon = Sprite(icons2, 20, 0, 20, 20).sprite
iron_col_icon = Sprite(icons2, 40, 0, 20, 20).sprite
gem_col_icon = Sprite(icons2, 60, 0, 20, 20).sprite