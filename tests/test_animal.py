from world_simulation.elements.base_elements import Animal

import pytest


def test_take_dmg():
	"""
		Tests taking damage
	"""
	x = Animal(100,'Male',1,1,1,1)

	x.take_dmg(10)
	assert x.health == 90


def test_heal():
	"""
		Tests heal functionallity
	"""
	x = Animal(100,'Male',1,1,1,1)

	x.take_dmg(10)
	assert x.health == 90

	x.heal(10)
	assert x.health == 100
	x.heal(10)	
	assert x.health == 100

	x.take_dmg(10)
	x.pass_time()
	x.move()
	x.eat(300)
	assert x.health == 100
	assert x.hunger == 0
	assert x.stamina == 1

def test_time():
	"""
		Tests passage of time, with hunger evolution, health loss and eating recovery
	"""
	x = Animal(101,'Male',1,1,100,1)

	x.pass_time()
	assert x.age == 1
	assert x.hunger == 100
	assert x.health == 101

	x.pass_time()
	assert x.age == 2

	assert x.hunger == 200
	assert x.health == 1

	x.eat(300)
	assert x.hunger == 0
	assert x.health == 101


def test_dead():
	x = Animal(100,'Male',1,1,100,1)

	x.pass_time()
	x.pass_time()
	assert x.health == 0
	assert x.is_alive == False

	x.pass_time()
	assert x.is_alive == False

	assert x.heal(10) == -1
	assert x.restore_stamina(10) == -1
	assert x.eat(100) == -1

def test_stamina():
	x = Animal(100,'Male',2,1,100,1)

	x.move()
	assert x.stamina == 1
	x.move()
	assert x.stamina == 0
	x.move()
	assert x.stamina == -1
	x.move()
	assert x.stamina == 0

	x.take_dmg(20)
	x.heal(30)
	assert x.health == 100
	assert x.stamina == 2