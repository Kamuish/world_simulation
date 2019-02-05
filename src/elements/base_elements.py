
class Animal():
	def __init__(self, health,sex,stamina,speed, hunger_per_tick, thirst_per_tick):
		self.max_health = health
		self.health = health
		self.age = 0

		self.hunger = 0
		self.thirst = 0
		self.speed = speed
		self.sex = sex 
		self.stamina = stamina 
		self.max_stamina = stamina
		
		self.hunger_per_tick = hunger_per_tick
		self.thirst_per_tick = thirst_per_tick
		self.cycle = 0

		self.state = 'awake' # awake/sleep/dead

	def pass_time(self):
		self.age += 1
		self.hunger += self.hunger_per_tick 

		if self.hunger > 100 : # animal is starving
			self.health -= self.hunger_per_tick

		# ToDo: implement growth and decay using the config file !!!!!!!!!!!

	def take_dmg(self,dmg):
		self.health -= dmg

	def heal(self, value):
		if not self.is_alive:
			print("Already dead")
			return

		new_health = min(self.max_health, self.health + value )
		print(new_health)
		if new_health == 0:
			self.restore_stamina(self.max_health - self.health )
		self.health = new_health

	def restore_stamina(self, value):
		if not self.is_alive:
			print("Already dead")
			return
		new_stam = min(self.max_stamina, self.stamina + value )

		self.stamina = new_stam


	def __repr__(self):
		return "State - {},health - {}, hunger - {}, stamina - {}".format(self.state, self.health, self.hunger, self.stamina)

	@property
	def animal_type(self):
		return self.type
	
	@property
	def is_alive(self):
		return self.health >= 0