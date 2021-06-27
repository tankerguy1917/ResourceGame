###### MAIN GAME FILE ######

#### Imports ####
import pygame, sys, copy
from pygame.locals import *
from ResourceGame.Assets.Images import *
from ResourceGame.Scripts.UI.ButtonClass import Button
from ResourceGame.Scripts.GameClass import Game
from ResourceGame.Scripts.Resources.ResourceClass import Producer, Collector

pygame.init()

#### Window Stuff ####
WIN = (600, 500)
screen = pygame.display.set_mode(WIN, 0, 32)

#### Clock ####
clock = pygame.time.Clock()

#### Main Menu ####
def main_menu():
	global WIN

	#### Font ####
	font = pygame.font.Font("ResourceGame/Assets/Fonts/PressStart2P.ttf", 8)

	#### Screen to display things ####
	menu_screen = pygame.Surface((WIN[0] // 4, WIN[1] // 4))

	#### Buttons ####
	start_button = Button(start_button_img1, 62, 38)
	cred_button = Button(cred_button_img1, 62, 48)

	while True:
		#### Gets mouse pos and puts mouse rect there ####
		mx, my = pygame.mouse.get_pos()
		mouse = pygame.Rect(mx // 4, my // 4, 1, 1)

		#### Clears/fills screen ####
		menu_screen.fill((0, 0, 0))

		#### Gets FPS to display ####
		fps = ("FPS: " + str(int(clock.get_fps())))
		fps2 = font.render(fps, False, (255, 255, 255))

		#### Displays FPS ####
		menu_screen.blit(fps2, (0, 0))

		#### Displays buttons ####
		start_button.display(menu_screen)
		cred_button.display(menu_screen)

		#### Checks for events ####
		for e in pygame.event.get():
			if e.type == QUIT:
				pygame.quit()
				sys.exit()
			if e.type == MOUSEBUTTONDOWN:
				if e.button == 1:
					if mouse.colliderect(start_button.button):
						print("game")
						game()
					elif mouse.colliderect(cred_button.button):
						print("credits")
						credits()

		#### Refreshes screen ####
		screen.blit(pygame.transform.scale(menu_screen, WIN), (0, 0))
		pygame.display.update()
		clock.tick(60)


#### Credits ####
def credits():
	global WIN

	#### Screen to display things ####
	credit_screen = pygame.Surface((WIN[0] // 2, WIN[1] // 2))

	#### Font ####
	font = pygame.font.Font("ResourceGame/Assets/Fonts/PressStart2P.ttf", 8)

	#### List of people and what they contributed ####
	credit_list = [
		["Made by tankerguy1917", 0, 80],
		["Font by Codeman38", 0, 105],
	]
	#### Just trust me on this one ####
	credit_list2 = []

	#### And this one too ####
	for cred in credit_list:
		text = font.render(cred[0], False, (255, 255, 255))
		credit_list2.append([text, cred[1], cred[2]])

	while True:
		#### Clears/fills screen ####
		credit_screen.fill((0, 0, 0))
		skip_message1 = "Press Esc"
		skip_message2 = "to skip"
		credit_screen.blit(font.render(skip_message1, False, (255, 255, 255)), (225, 0))
		credit_screen.blit(font.render(skip_message2, False, (255, 255, 255)), (225, 10))

		#### Checks for events ####
		for e in pygame.event.get():
			if e.type == QUIT:
				pygame.quit()
				sys.exit()
			if e.type == KEYDOWN:
				if e.key == K_ESCAPE:
					main_menu()

		#### Displays credits and moves them ####
		for text in credit_list2:
			credit_screen.blit(text[0], (text[1], text[2]))
			text[2] -= 0.5

		#### Checks if credits have finished ####
		if credit_list2[-1][2] < -20:
			main_menu()

		#### Refreshes screen ####
		screen.blit(pygame.transform.scale(credit_screen, WIN), (0, 0))
		pygame.display.update()
		clock.tick(60)


#### Where the fun begins ####
def game():
	global WIN
	game_screen = pygame.Surface((WIN[0] // 2, WIN[1] // 2))
	game = Game(WIN[0] // 2, WIN[1] // 2, 20)

	#### Resources ####
	tree_col = Collector()
	stone_col = Collector()
	iron_col = Collector()
	gem_col = Collector()

	#### Adds resources to game.resource_list, so you can collect resources ####
	game.resource_list = [tree_col, stone_col, iron_col, gem_col]

	#### This is needed to buy and place resource collecotrs ####
	current_img = None

	#### Collect/Sell buttons ####
	collect_button = Button(collect_button_img, 275, 0)
	sell_button = Button(sell_button_img, 275, 15)

	#### Font ####
	font = pygame.font.Font("ResourceGame/Assets/Fonts/PressStart2P.ttf", 8)

	while True:
		#### Gets mouse 1s position ####
		mx, my = pygame.mouse.get_pos()
		mouse = pygame.Rect(mx // 2 - 40, my // 2 - 30, 1, 1)

		#### Gets mouse 2s position ####
		mx2, my2 = pygame.mouse.get_pos()
		mouse2 = pygame.Rect(mx2 // 2, my2 // 2, 1, 1)

		#### Clears/fills screens
		game_screen.fill((0, 0, 0))
		game.screen.fill((0, 255, 0))

		#### Gets FPS to display ####
		fps = ("FPS: " + str(int(clock.get_fps())))
		fps2 = font.render(fps, False, (255, 255, 255))

		#### Displays FPS ####
		game_screen.blit(fps2, (0, 0))

		#### Displays resource icons ####
			## Wood ##
		game_screen.blit(wood_icon, (28, 13))
		wood_amount = str(game.resource_list[0].amount)
		game_screen.blit(font.render(wood_amount, False, (255, 255, 255)), (43, 16))
			## Stone ##
		game_screen.blit(stone_icon, (70, 13))
		stone_amount = str(game.resource_list[1].amount)
		game_screen.blit(font.render(stone_amount, False, (255, 255, 255)), (85, 16))
			## Iron ##
		game_screen.blit(iron_icon, (113, 14))
		iron_amount = str(game.resource_list[2].amount)
		game_screen.blit(font.render(iron_amount, False, (255, 255, 255)), (129, 16))
			## Gems ##
		game_screen.blit(gem_icon, (155, 13))
		gem_amount = str(game.resource_list[3].amount)
		game_screen.blit(font.render(gem_amount, False, (255, 255, 255)), (172, 16))
			## Money ##
		game_screen.blit(money_icon, (205, 11))
		money_amount = str(game.money)
		game_screen.blit(font.render(money_amount, False, (255, 255, 255)), (220, 16))

		#### Displays collect/sell buttons ####
		collect_button.display(game_screen)
		sell_button.display(game_screen)

		#### Displays shop icons ####
			## Wood ##
		wood_buy_rect = pygame.Rect(0, 33, 40, 33)
		game_screen.blit(wood_col_icon, (5, 30))
		wood_cost = 50
		true_wood_cost = "$ " + str(wood_cost)
		game_screen.blit(font.render(true_wood_cost, False, (255, 255, 255)), (0, 58))
			## Stone ##
		stone_buy_rect = pygame.Rect(0, 76, 40, 40)
		game_screen.blit(stone_col_icon, (5, 70))
		stone_cost = 100
		stone_w_cost = 50
		true_stone_cost = "$ " + str(stone_cost)
		true_stone_w_cost = "W " + str(stone_w_cost)
		game_screen.blit(font.render(true_stone_cost, False, (255, 255, 255)), (0, 98))
		game_screen.blit(font.render(true_stone_w_cost, False, (255, 255, 255)), (0, 108))
			## Iron ##
		iron_buy_rect = pygame.Rect(0, 126, 40, 52)
		game_screen.blit(iron_col_icon, (5, 120))
		iron_cost = 200
		iron_w_cost = 100
		iron_s_cost = 75
		true_iron_cost = "$ " + str(iron_cost)
		true_iron_w_cost = "W " + str(iron_w_cost)
		true_iron_s_cost = "S " + str(iron_s_cost)
		game_screen.blit(font.render(true_iron_cost, False, (255, 255, 255)), (0, 148))
		game_screen.blit(font.render(true_iron_w_cost, False, (255, 255, 255)), (0, 158))
		game_screen.blit(font.render(true_iron_s_cost, False, (255, 255, 255)), (0, 168))
			## Gems ##
		gem_buy_rect = pygame.Rect(0, 186, 40, 65)
		game_screen.blit(gem_col_icon, (0, 180))
		gem_cost = 500
		gem_w_cost = 250
		gem_s_cost = 130
		gem_i_cost = 80
		true_gem_cost = "$ " + str(gem_cost)
		true_gem_w_cost = "W " + str(gem_w_cost)
		true_gem_s_cost = "S " + str(gem_s_cost)
		true_gem_i_cost = "I " + str(gem_i_cost)
		game_screen.blit(font.render(true_gem_cost, False, (255, 255, 255)), (0, 208))
		game_screen.blit(font.render(true_gem_w_cost, False, (255, 255, 255)), (0, 218))
		game_screen.blit(font.render(true_gem_s_cost, False, (255, 255, 255)), (0, 228))
		game_screen.blit(font.render(true_gem_i_cost, False, (255, 255, 255)), (0, 238))

		#### Displays resource collcetor icons ####
		for res in game.resource_list:
			for prod in res.prod_list:
				game.screen.blit(prod.img, prod.loc)

		#### Displays where resource collector will be placed ####
		if current_img != None:
			for rect in game.rect_list:
				if mouse.colliderect(rect):
					game.screen.blit(current_img, (rect[0], rect[1]))

		#### Checks for events ####
		for e in pygame.event.get():
			if e.type == QUIT:
				pygame.quit()
				sys.exit()
			if e.type == KEYDOWN:
				if e.key == K_RETURN:
					for res in game.resource_list:
						res.collect()
				if e.key == K_SPACE:
					game.money += int(game.resource_list[0].amount * 5)
					game.money += int(game.resource_list[1].amount * 5)
					game.money += int(game.resource_list[2].amount * 7)
					game.money += int(game.resource_list[3].amount * 11)
					for res in game.resource_list:
						res.amount = 0
			if e.type == MOUSEBUTTONDOWN:
				if e.button == 1:
					if mouse2.colliderect(collect_button.button):
						for res in game.resource_list:
							res.collect()
					elif mouse2.colliderect(sell_button.button):
						game.money += int(game.resource_list[0].amount * 5)
						game.money += int(game.resource_list[1].amount * 5)
						game.money += int(game.resource_list[2].amount * 7)
						game.money += int(game.resource_list[3].amount * 11)
						for res in game.resource_list:
							res.amount = 0
					elif mouse2.colliderect(wood_buy_rect):
						if game.money >= wood_cost:
							current_img = wood_col_icon
							game.money -= wood_cost
					elif mouse2.colliderect(stone_buy_rect):
						if game.money >= stone_cost:
							if game.resource_list[0].amount >= stone_w_cost:
								current_img = stone_col_icon
								game.money -= stone_cost
								game.resource_list[0].amount -= stone_w_cost
					elif mouse2.colliderect(iron_buy_rect):
						if game.money >= iron_cost:
							if game.resource_list[0].amount >= iron_w_cost:
								if game.resource_list[1].amount >= iron_s_cost:
									current_img = iron_col_icon
									game.money -= iron_cost
									game.resource_list[0].amount -= iron_w_cost
									game.resource_list[1].amount -= iron_s_cost
					elif mouse2.colliderect(gem_buy_rect):
						if game.money >= gem_cost:
							if game.resource_list[0].amount >= gem_w_cost:
								if game.resource_list[1].amount >= gem_s_cost:
									if game.resource_list[2].amount >= gem_i_cost:
										current_img = gem_col_icon
										game.money -= gem_cost
										game.resource_list[0].amount -= gem_w_cost
										game.resource_list[1].amount -= gem_s_cost
										game.resource_list[2].amount -= gem_i_cost
					for rect in game.rect_list:
						if current_img != None:
							if mouse.colliderect(rect):
								if current_img == wood_col_icon:
									game.resource_list[0].prod_list.append(Producer((rect[0], rect[1]), wood_col_icon, 5))
									current_img = None
								if current_img == stone_col_icon:
									game.resource_list[1].prod_list.append(Producer((rect[0], rect[1]), stone_col_icon, 2))
									current_img = None
								if current_img == iron_col_icon:
									game.resource_list[2].prod_list.append(Producer((rect[0], rect[1]), iron_col_icon, 2))
									current_img = None
								if current_img == gem_col_icon:
									game.resource_list[3].prod_list.append(Producer((rect[0], rect[1]), gem_col_icon, 1))
									current_img = None

		#### Updates screen ####
		screen.blit(pygame.transform.scale(game_screen, WIN), (0, 0))
		game_screen2 = copy.copy(game.screen)
		screen.blit(pygame.transform.scale(game_screen2, WIN), (80, 60))
		pygame.display.update()
		clock.tick(60)

main_menu()