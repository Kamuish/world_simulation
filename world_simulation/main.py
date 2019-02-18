from elements import Carnivore

from Map import Map, plot_carnivores, plot_all

def main():
	game_map = Map(4)
	aa = Carnivore(health = 1, sex = 'Male', stamina = 1,speed = 1,hunger_tick = 101, thirst_tick = 1, fov_radius = 1)

	game_map.place_animal(1,1,aa)
	game_map.place_animal(2,2,aa)

	plot_all(game_map)

	game_map.pass_time()

	plot_all(game_map, which = 'dead')
	
main()