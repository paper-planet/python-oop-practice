from main import *
from fx import clear_screen, animate_screen, color

RED = "\033[31m"	#color
GREEN = "\033[32m"	#color
RESET = "\033[0m"	#color

class Manage:
	def __init__(self):
		clear_screen
		x = Player("X", element='fire')
		y = Player("Y", element='water')
		turn_counter = 0

		while x.health > 0 and y.health > 0:
			animate_screen()				
			turn_counter += 1			
			print(f"|=========-------- Turn {turn_counter} --------=========|")			
			x.take_turn(y)
			if y.health <= 0:
				break			
			print(f"|=========-------- Turn {turn_counter} --------=========|")			
			y.take_turn(x)
		
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