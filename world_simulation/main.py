from elements import Carnivore

from Map import Map

def main():
	game_map = Map(4)

	aa = Carnivore(1,1,1,1,1,1)
	game_map.place_animal(1,1,aa)

	print(game_map.cells[1,1].animals[0])
main()