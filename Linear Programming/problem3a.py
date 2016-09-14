import numpy as np

from scipy.optimize import linprog

# a, b, c, d, e, f, g, h, i, j, k, l, m
f = np.array([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1])

# calculates the shortest path from a to all vertices
A = np.array([[-1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[-1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[-1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[-1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
			[1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, -1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, -1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, -1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
			[0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
			[0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
			[1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
			[0, 0, 0, -1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0],
			[0, 0, 1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, -1, 1, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 1, 0, 0, -1, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0],
			[1, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 1, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 1],
			[0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 1, 0],
			[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 1],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1],
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]])

b = np.array([[2], [3], [8], [9], [4], [5], [7], [4], [10],
			[5], [9], [11], [4], [8], [2], [5], [1], [5],
			[4], [10], [2], [2], [2], [8], [12], [5], [10],
			[20], [6], [2], [12], [2], [4], [5], [10], [10],
			[2], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]])

res = linprog(f, A, b)

print(res)
