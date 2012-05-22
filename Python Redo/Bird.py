import random

class Bird:

	def __init__(self):
		self.reserves = 0
		self.points = 0
		self.has_mate = False

	def sing(self):
		B = self.get_B()
		D = 12 + (0.002 * self.reserves) + B
		self.use_food(D)

	def forage(self):
		B = self.get_B()
		D = 8 + (0.007 * self.reserves) + B
		self.use_food(D)
		self.gain_random_food()
		

	def gain_random_food(self):
		rand_int = random.randint(0, 100)
		if (rand_int <= 60):
			self.reserves += 32


	def rest(self):
		D = 3.6
		self.use_food(D)

	def use_food(self, food):
		self.reserves = self.reserves - food

	def get_B(self):
		rand_num = random.randint(0, 100)
		if rand_num < 50:
			return -6.4
		elif (rand_num >= 50) and (rand_num < 75):
			return 0.0
		else:
			return 6.4

	def pair_with_mate(self):
		self.has_mate = random.randint(10000) > 4

	def has_food_for_night(self):
		return self.reserves > (3.6 * 75)

	def is_dead(self):
		return self.reserves <= 0

	def calculate_points(self):
		if self.has_mate and not self.is_dead():
			self.points += 2
		elif not self.is_dead():
			self.points += 1
		else:
			self.points += 0

class World:

	def __init__(self):
		self.time = 0

	def advance_time(self):
		self.time += 1

	def is_nighttime(self):
		return self.time > 75

	def is_finished(self):
		return self.time >= 150



for i in range(0, 100):
	random.seed(2)
	world = World()
	bird = Bird()

	birds_actions = []
	while (world.is_finished() is False):

		if world.is_nighttime():
			birds_actions.append("REST")
			bird.rest()

		else:
			if bird.has_food_for_night():
				birds_actions.append("SING")
				bird.sing()
			else:
				birds_actions.append("FORAGE")
				bird.forage()

		


		if (bird.is_dead()):
			break

		world.advance_time()

	if bird.is_dead:
		print "Bird died, but had mate = " + str(bird.has_mate) + " " + str(bird.reserves) + " reserves"
	else:
		print "Bird is alive, but had mate = " + str(bird.has_mate) + " " + str(bird.reserves) + " reserves"

