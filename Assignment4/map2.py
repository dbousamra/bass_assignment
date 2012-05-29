def create_grid(x, y):
	g = []
	for i in range(0, y):
		g.append([])
		for y in range(0, x):
			g[i].append(0)

	return g

grid = create_grid(9, 9)

distances = [[0, 4, 7],
			 [4, 0, 9],
			 [7, 9, 0]]
A = 0
B = 1
C = 2


names = ["A", "B", "C"]


def get_distance(point1, point2):
	return str(distances[point1][point2])

def print_constraints(point):
	for x in range(0, len(distances[point])):
		print "Constraint " + names[point] + " => " + names[x] + " = " + str(distances[point][x])

def get_constraints(point):
	return distances[point]





for point in range(A, C+1):
	print point 