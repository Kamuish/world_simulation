from base_elements import Animal

class Carnivore(Animal):
	def __init__(self, health,sex,stamina,hunger_tick, thirst_tick):
		super().__init__(health, sex, stamina,hunger_tick, thirst_tick)

		self.type = 'Carnivore'


	def eat(self,prey_health):
		new_hunger = min(0,abs(self.hunger - prey_health))
		
		if new_hunger == 0:
			self.heal(prey_health - self.hunger )

		self.hunger =  new_hunger


if __name__ == '__main__':
	x = Carnivore(10,1,1,10,1)
	x.pass_time()
	print(x)
	x.pass_time()
	x.take_dmg(2)
	print(x)
	x.eat(30)
	print(x)
