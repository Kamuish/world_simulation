from .base_elements import Animal

class Carnivore(Animal):
	def __init__(self, health,sex,stamina,speed,hunger_tick, thirst_tick, fov_radius):
		super().__init__(health, sex, stamina,speed,hunger_tick, thirst_tick,fov_radius)

		self.type = 'Carnivore'


	

if __name__ == '__main__':
	x = Carnivore(10,1,1,1,10,1)
	x.pass_time()
	print(x)
	x.pass_time()
	x.take_dmg(2)
	print(x)
	x.eat(30)
	print(x)
