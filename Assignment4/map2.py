import random
import math

class Grid:

    def __init__(self, width, height):
        self.grid = self.create_grid(width, height)
        self.width = width
        self.height = height

    def print_grid(self):
        for row in self.grid:
            print row

    def create_grid(self, x, y):
        g = []
        for i in range(0, y):
            g.append([])
            for y in range(0, x):
                g[i].append(-1)

        return g

    def place_on_grid(self, x, y, point, g):
        self.grid[x][y] = point
        self.x = x
        self.y = y


    def get_coordinate_of_point(self, point_integer):
        for i, row in enumerate(self.grid):
            if point_integer in row:
                return (row.index(point_integer), self.height)

    def get_distance_between_points(self, point1, point2):
        return math.sqrt( ((point2[0] - point1[0]) ** 2)  + ((point2[1] - point1[1]) ** 2) )

    def startingpoint(self, names):
        for i in range(0, len(names) - 1):
            x1 = random.randint(0,len(self.grid)-1)
            y1 = random.randint(0,len(self.grid)-1)
            self.grid[x1][y1] = names[i]

grid = Grid(9, 9)


distances = [[0, 4, 3],
             [4, 0, 2],
             [3, 2, 0]]
A = 0
B = 1


#names = ["A", "B", "C"]
names = [1,10]

def get_distance(point1, point2):
    return str(distances[point1][point2])

def print_constraints(point):
    for x in range(0, len(distances[point])):
        print "Constraint " + str(names[point]) + " => " + str(names[x]) + " = " + str(distances[point][x])

def get_constraints(point):
    return distances[point]
            
def fitness(point1):
    direction = (0, 0)
    actual_position_point1 = grid.get_coordinate_of_point(point1)

    


def mutate(correctpoint, startingpoint):
     if fitval != 0:
        m = len(correctpoint)
        j = random.randint(0,m-1)
        return correctpoint[0:j]+str(1-int(correctpoint[j]))+correctpoint[j+1:m]
     else:
        return correctpoint


grid.startingpoint(names)
fitness(0)