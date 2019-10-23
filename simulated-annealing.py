import matplotlib.pyplot as plt
import math
import random


def plot_path(path):
    for i in range(0, len(path)):
        plt.plot((path[i][0], path[(i + 1) % len(path)][0]), (path[i][1], path[(i + 1) % len(path)][1]))

def probability(current, neighbour, tempurature):
    return min(math.exp((path_length(current) - path_length(neighbour))/tempurature), 1)


def distance(p1, p2):
    (x1, y1) = p1
    (x2, y2) = p2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def path_length(path):
    dist = 0
    for i in range(0, len(path)):
        dist += distance(path[i], path[(i + 1) % len(path)])

    return dist
    

def simulated_annealing(cities, max_iterations=100):
    tempurature = 10
    start = cities[:]
    random.shuffle(start)
    for i in range(max_iterations):
        plt.clf()
        plot_path(start)
        plt.title(f'Iteration {i}, length = {path_length(start)}')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.savefig(f'plots/iteration-{i}.png')
        next = start[:]
        j, k = random.randint(0, len(next) - 1), random.randint(0, len(next) - 1)
        next[j], next[k] = next[k], next[j]
        uniform_sample = random.random()
        if uniform_sample <= probability(start, next, tempurature):
            start = next
        tempurature -= 1 / (max_iterations + 1)

cities = []
for i in range(100):
    x, y = random.randint(1, 100), random.randint(1, 100)
    cities.append((x, y))

simulated_annealing(cities, max_iterations=1000)
