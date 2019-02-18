
class Tile():
	def __init__(self, tile_type):
		"""
			Tile in the game map

			Arguments
			=========

			tile_type:
				water/land
		"""
		
		self.coords = None

		self.plants = []
		self.animals = []
		self.dead_animals = []
		self.tile_type = tile_type


	@property
	def is_land(self):
		return self.tile_type == 'Land'
	
	def place(self,X,Y):
		self.coords = (X,Y)

	def new_animal(self, animal):
		"""
			Adds an animal to the tile
		"""
		self.animals.append(animal)

	def new_plant(self, plant):
		"""
			Adds an plant to the tile
		"""
		self.plants.append(plant)


	def get_carnivores(self, which):
		count = 0

		if which == 'alive':
			animals_to_search = self.animals
		else:
			animals_to_search = self.dead_animals
		for j in animals_to_search:
			if j.animal_type == 'Carnivore':
				count +=1 
		return count

	def pass_time(self):
		remove = [] # going to store the indexes to remove
		for i in range(len(self.animals)):
			self.animals[i].pass_time()
			if not self.animals[i].is_alive:
				remove.append(i)
				self.dead_animals.append(self.animals[i])

		for rm in remove:
			self.animals.pop(rm)
		for dead_animal in self.dead_animals: # implement decay of the body
			dead_animal.pass_time()	

	@property
	def live_creatures(self):
		return self.animals

	@property
	def dead_creatures(self):
		return self.dead_animals
	
	@property
	def total_animals(self):		
		return len(self.animals)

	
		
	def __repr__(self):
		return "Tile in position {} with {} live animals and {} plants".format(self.coords, len(self.animals), len(self.plants))



			
class Water_Tile(Tile):
	def __init__(self):
		super().__init__(tile_type = 'Water')

	
class Terrain_Tile(Tile):
	def __init__(self):
		super().__init__(tile_type = 'Land')
