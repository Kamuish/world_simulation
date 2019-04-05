
class Animal():
	def __init__(self, health,sex,stamina,speed, hunger_per_tick, thirst_per_tick, fov_radius ):
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

		self.current_position = []
		self.field_of_view = fov_radius

	def search_for_destiny(self):
		"""
		Searches on previously defined field of view for the best direction to go.
		This method is defined on the Child classes that use this as a parent
		"""
		pass

		
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
			return -1

		new_health = min(self.max_health, self.health + value )
		if new_health == self.max_health:
			self.restore_stamina(self.max_health - self.health )
		self.health = new_health
		return 0

	def move(self):
		if self.stamina < 0:
			# dont move
			self.stamina += self.speed
		else:
			self.stamina -= self.speed
	def restore_stamina(self, value):
		if not self.is_alive:
			print("Already dead")
			return -1
		new_stam = min(self.max_stamina, self.stamina + value )

		self.stamina = new_stam
		return 0
		
	def eat(self,prey_health):
		if not self.is_alive:
			print("Already dead")
			return -1

		new_hunger = min(0,abs(self.hunger - prey_health))
		
		if new_hunger == 0:
			self.heal(prey_health - self.hunger )

		self.hunger =  new_hunger
		return 0

	def __repr__(self):
		return "State - {},health - {}, hunger - {}, stamina - {}".format(self.state, self.health, self.hunger, self.stamina)

	@property
	def animal_type(self):
		return self.type
	
	@property
	def is_alive(self):
		return self.health > 0


	