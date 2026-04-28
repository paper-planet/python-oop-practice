from random import randint
from fx import clear_screen, roll, animate_roll, animate_screen, color

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

	def calc_element_crit(self, target): # 1/3 odds hitting crit if advantage element.
		if self.element == 'water' and target.element == 'fire':
			return True if roll(1, 3) == 3 else False
		elif self.element == 'fire' and target.element == 'grass':
			return True if roll(1, 3) == 3 else False
		elif self.element == 'grass' and target.element == 'water':
			return True if roll(1, 3) == 3 else False

		
	def basic_attack(self, target):		
		damage = roll(1, 100)		
		animate_roll(damage)		

		if self.calc_element_crit(target) == True:
			print(f"Critical Hit, {damage} DMG +50%")
			damage *= round(1.5) # +50% damage on 1/3odds crit hit.
		target_prev_hp = target.health
		target.health -= damage		

		return f"""
| - - - - - - -Basic Attack- - - - - - - - |
|			
|  {self.name} ---Attacking---> {target.name} 	     
|  {target.name}: HP = {target_prev_hp} - ({damage} DMG) 
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
		
		crit_multiplier = self.calc_element_crit(target)
		crit_output = 'Miss'

		if power_charge <= self.power and power_charge != 1:
			self.power -= power_charge		
			damage = roll(1, 35)
			animate_roll(damage)
			super_damage = damage * power_charge
			if crit_multiplier == True:
				crit_output = f'{damage} DMG +50%'
				super_damage *= round(1.5) # +50% damage on 1/3odds crit hit.	
			target_prev_hp = target.health
			target.health -= super_damage		

		elif power_charge == 1:
			self.power -= power_charge		
			damage = roll(1, 35)
			animate_roll(damage)
			super_damage = damage * 2
			if crit_multiplier == True:
				crit_output = f'{damage} DMG +50%'
				damage *= round(1.5) # +50% damage on 1/3odds crit hit.					
			target_prev_hp = target.health
			target.health -= super_damage		
		else:
			return 'Not Enough Power For Super Attack.'
		
		return f"""
|------------| Super Attack |--------------$
||			
||  {self.name} ---Attacking---> {target.name} 	     
||  Power Charge: {power_charge}
||  Critical Hit: {crit_output}
||  {target.name}: HP = {target_prev_hp} - ({damage} DMG * {power_charge} POWER) = {damage * power_charge}
||  {target.name}: HP Now = {target.health}	
||  {self.name} New Available Power: {self.power}
||   
|-----------| Finished Attack |------------$ 
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
		


