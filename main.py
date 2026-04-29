from random import randint
from fx import clear_screen, roll, animate_roll
from time import sleep

class Object:
	def __init__(self, name):
		self.name = name
	
	def stats(self):
		clear_screen()
		return f"""
|==========---{self.name} Stats---============|
{self}
|=========---End {self.name} Stats---=========|
"""
	
class Player(Object):

	ADVANTAGE = {
    		"water": "fire",
    		"fire": "grass",
    		"grass": "water"
	}

	def __init__(self, *args,  element='basic', health=1000, power=100, **kwargs):
		super().__init__(*args, **kwargs)
		self.element = element		
		self.health = health
		self.power = power
		
	def __str__(self):
		return f"""
Player {self.name}
Element: {self.element}
HP = {self.health}
Power = {self.power}
"""

	def calc_element_crit(self, target):
		if self.ADVANTAGE.get(self.element) == target.element:
	        	return roll(1, 3) == 3
		return False

	def apply_damage(self, target, base_damage, multiplier=1):
		crit = self.calc_element_crit(target)

		damage = base_damage * multiplier

		if crit:
			damage = int(damage * 1.5)

		target_prev_hp = target.health
		target.health -= damage

		return damage, target_prev_hp, crit

	def basic_attack(self, target):
		base_damage = roll(1, 100)
		animate_roll(base_damage)

		damage, prev_hp, crit = self.apply_damage(target, base_damage)

		crit_output = f"{base_damage} DMG +50%" if crit else "Miss"

		return f"""
| - - - - - - -{self.name} Basic Attack- - - - - - - - |
|
|  {self.name} ---Attacking---> {target.name}
|  Critical Hit: {crit_output}
|  {target.name}: HP = {prev_hp} - ({damage} DMG)
|  {target.name}: HP Now = {target.health}
|
| - - - - - - {self.name} Finished Basic Attack - - - - - - -|
"""	

	def super_attack(self, target, auto=False):
		print('|--------------Super Attack----------------|')
		print(f'How Much Power? {self.power} available:')

		if auto:
			power_charge = randint(0, self.power)
		else:
			try:
				power_charge = int(input('--->'))
			except ValueError:
				return '\nIncorrect Data Type For Power\n'

		if power_charge > self.power:
			return 'Not Enough Power For Super Attack.'

		self.power -= power_charge

		base_damage = roll(1, 35)
		animate_roll(base_damage)

		# normalize multiplier
		multiplier = 2 if power_charge == 1 else power_charge

		damage, prev_hp, crit = self.apply_damage(target, base_damage, multiplier)

		crit_output = f"{base_damage} DMG +50%" if crit else "Miss"

		return f"""
|------------| {self.name} Super Attack |--------------|
|
|  {self.name} ---Attacking---> {target.name}
|  Power Charge: {power_charge}
|  Critical Hit: {crit_output}
|  {target.name}: HP = {prev_hp} - ({damage} DMG)
|  {target.name}: HP Now = {target.health}
|  {self.name} New Available Power: {self.power}
|
|-----------| {self.name} Finished Attack |------------|
"""
	
	def heal(self):
		old_hp = self.health
		influx = roll(10, 420)
		animate_roll(influx)
		self.health += influx		
		return f"""
|<3--------------{self.name} Healing-----------------<3|
|						       
|  {self.name}: {old_hp} + {influx} HP 	       
|  {self.name}: HP Now = {self.health}	       
|						       
|<3-----------{self.name} Finished Healing-----------<3|
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
		if x == '1':
			print(f'{self.stats()}{target.stats()}')
			self.take_turn(target)		
		elif x == '2':
			print(self.heal())
		elif x == '3':
			print(self.basic_attack(target))
		elif x == '4':
			print(self.super_attack(target))
		else:
			print('Invalid. End of Turn.')
		
class AI(Player):
	def take_turn(self, target):
		print(f'\n{self.name} Taking Turn...\n')
		sleep(1)		
		x = roll(2, 4)				
		if x == 2:
			print(self.heal())
		elif x == 3:
			print(self.basic_attack(target))
		else:
			print(self.super_attack(target, auto=True))

