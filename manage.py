from main import *
from fx import clear_screen, animate_screen, color
from random import choice
from time import sleep

RED = "\033[31m"	#color
GREEN = "\033[32m"	#color
RESET = "\033[0m"	#color
ELEMENTS = ['grass', 'water', 'fire', 'basic']

class Manage:
	def __init__(self):
		clear_screen()

	def char_constructor(self):
		mode = input("""
Choose Mode:
	1: PVP
	2: PVE
--> 
""")
		if mode == '1':			
			x = Player(input('P1 Enter Name: '), element=input("Choose Element ('grass', 'water', 'fire') --> "))
			y = Player(input('P2 Enter Name: '), element=input("Choose Element ('grass', 'water', 'fire') --> "))
			return x, y

		else:
			x = Player(input('P1 Enter Name: '), element=input("Choose Element ('grass', 'water', 'fire') --> "))
			y = AI('AI', element=choice(ELEMENTS))
			return x, y

	def game_loop(self):	
		turn_counter = 0
		x, y = self.char_constructor()	
		while x.health > 0 and y.health > 0:	
			clear_screen()	
			turn_counter += 1			
			print(f"|=========-------- Turn {turn_counter} --------=========|")			
			x.take_turn(y)
			if x.health <= 0 or y.health <= 0:
				break			
			print(f"|=========-------- Turn {turn_counter} --------=========|")			
			y.take_turn(x)
			input('Continue?')
			
		
		print(f"""{RED}
|----------------Game Over-------------------
|
|   {GREEN}GAME STATS:{RED}
|
|   {GREEN}{x.name} HP: {RED}{x.health}
|   {GREEN}Remaining Power: {RED}{x.power}
|
|   {GREEN}{y.name} HP: {RED}{y.health}
|   {GREEN}Remaining Power: {RED}{y.power}
|
|   Game Ended In {GREEN}{turn_counter} {RED}Turns.
|   {GREEN}Thanks For Playing.{RED}
|----------------Game Over-------------------
{RESET}""")