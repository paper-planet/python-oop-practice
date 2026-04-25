from random import randint
from fx import clear_screen, roll, animate_roll, animate_screen, color

class Object:
	def __init__(self, name):
		self.name = name
	
	def stats(self):
		clear_screen()
		return f"""
|==========---Player {self.name} Stats---============|
{self}
|=========---End Player {self.name} Stats---=========|
"""
	
class Player(Object):
	def __init__(self, *args, health=1000, power=100, **kwargs):
		super().__init__(*args, **kwargs)
		self.health = health
		self.power = power

	def __str__(self):
		return f"""
Player {self.name}
HP = {self.health}
Power = {self.power}
"""

	def heal(self):
		old_hp = self.health
		influx = roll(1, 50)
		animate_roll(influx)
		self.health += influx		
		return f"""
|<3--------------Healing-----------------<3|
|						       
|  {self.name}: {old_hp} + {influx} HP 	       
|  {self.name}: HP Now = {self.health}	       
|						       
|<3-----------Finished Healing-----------<3|
"""

	def basic_attack(self, target):
		damage = roll(1, 100)
		animate_roll(damage)
		target_prev_hp = target.health
		target.health -= damage		
		return f"""
| - - - - - - -Basic Attack- - - - - - - - |
|			
|  {self.name} ---Attacking---> {target.name} 	     
|  {target.name}: HP = {target_prev_hp} - {damage} DMG 
|  {target.name}: HP Now = {target.health}	     
|
| - - - - - - Finished Attack - - - - - - -|
"""

	def super_attack(self, target):	
		print("|--------------Super Attack----------------|")
		print(f'How Much Power? {self.power} available:')
		try:		
			power_charge = int(input('--->'))
		except ValueError:
			return '\nIncorrect Data Type For Power\n'

		# power_charge = randint(1, self.power)		
		
		if power_charge <= self.power and power_charge != 1:
			self.power -= power_charge		
			damage = roll(1, 35)
			animate_roll(damage)
			super_damage = damage * power_charge
			target_prev_hp = target.health
			target.health -= super_damage		
		elif power_charge == 1:
			self.power -= power_charge		
			damage = roll(1, 35)
			animate_roll(damage)
			super_damage = damage * 2				
			target_prev_hp = target.health
			target.health -= super_damage		
		else:
			return 'Not Enough Power For Super Attack.'
		
		return f"""
|------------| Super Attack |--------------$
||			
||  {self.name} ---Attacking---> {target.name} 	     
||  Power Charge: {power_charge}
||  {target.name}: HP = {target_prev_hp} - ({damage} DMG * {power_charge} POWER) = {damage * power_charge}
||  {target.name}: HP Now = {target.health}	
||  {self.name} New Available Power: {self.power}
||   
|-----------| Finished Attack |------------$ 
"""
	
	def take_turn(self, target):
		print(f"""
|=====------------{self.name}'s Turn------------=====|
Options (Select Number + Enter Key):
	Check Stats:  1	
	Heal:	      2				
	Basic Attack: 3
	Super Attack: 4 (Costs Power)
""")
		x = input('--->')
		clear_screen()
		#x = str(randint(1, 4))
		if x == '1':
			animate_screen()
			print(f'{self.stats()}{target.stats()}')
			self.take_turn(target)		
		elif x == '2':
			animate_screen()
			print(self.heal())
		elif x == '3':
			animate_screen()
			print(self.basic_attack(target))
		elif x == '4':
			animate_screen()
			print(self.super_attack(target))
		else:
			animate_screen()
			print('Invalid. End of Turn.')
		


