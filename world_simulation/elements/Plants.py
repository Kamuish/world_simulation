
class Plant():
	def __init__(self, health):
		self.health = health

		self.nutrients = 0 # will gain nutrients until it grows

	def pass_time(self):
		"""
			Will gain nutrients as a function of the terrain it's in
		"""
		pass

	def grow(self):
		self.nutrients = 0

	def take_dmg(self, dmg ):
		"""
			Someone is eating the plant
		"""
		self.health -= dmg