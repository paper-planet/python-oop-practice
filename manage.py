from main import *
from fx import animate_screen
import os

class Manage:
	def __init__(self):
		os.system('cls' if os.name == 'nt' else 'clear')
		x = Player("X")
		y = Player("Y")
		turn_counter = 0

		while x.health > 0 and y.health > 0:		
			os.system('cls' if os.name == 'nt' else 'clear')
			animate_screen()				
			turn_counter += 1			
			print(f"|=========-------- Turn {turn_counter} --------=========|")			
			x.take_turn(y)
			if y.health <= 0:
				break			
			print(f"|=========-------- Turn {turn_counter} --------=========|")			
			y.take_turn(x)
			os.system('cls' if os.name == 'nt' else 'clear')
		
		print(f"""
|----------------Game Over-------------------
|
|   GAME STATS:
|
|   {x.name} HP: {x.health}
|   Remaining Power: {x.power}
|
|   {y.name} HP: {y.health}
|   Remaining Power: {y.power}
|
|   Game Ended In {turn_counter} Turns.
|   Thanks For Playing.
|----------------Game Over-------------------
""")