from main import *
from fx import clear_screen, animate_screen

class Manage:
	def __init__(self):
		clear_screen
		x = Player("X")
		y = Player("Y")
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