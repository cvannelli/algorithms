import numpy as np

from scipy.optimize import linprog


f = np.array([1, 0.75, 0.50, 0.50, 0.45, 2.15, 0.95, 2.00])

A = np.array([[-0.85, -1.62, -2.86, -0.93, -23.4, -16.00, -9.00, 0],
			[-0.33, -0.20, -0.39, -0.24, -48.7, -5.00, -2.6, -100.00],
			[0.33, 0.20, 0.39, 0.24, 48.7, 5.00, 2.6, 100.00],
			[-4.64, -2.37, -3.63, -9.58, -15.00, -3.00, -27.0, 0],
			[9.00, 28.00, 65.00, 69.00, 3.80, 120.00, 78.00, 0],
			[0.40, -0.60, -0.60, 0.40, 0.40, 0.40, 0.40, 0.40],
			[21, 16, 40, 41, 585, 120, 164, 884],
			[-1, 0, 0, 0, 0, 0, 0, 0],
			[0, -1, 0, 0, 0, 0, 0, 0],
			[0, 0, -1, 0, 0, 0, 0, 0],
			[0, 0, 0, -1, 0, 0, 0, 0],
			[0, 0, 0, 0, -1, 0, 0, 0],
			[0, 0, 0, 0, 0, -1, 0, 0],
			[0, 0, 0, 0, 0, 0, -1, 0],
			[0, 0, 0, 0, 0, 0, 0, -1]])

b = np.array([[-15], [-2], [8], [-4], [200], [0], [249.9], [0], [0], [0], [0], [0], [0], [0], [0]])


res = linprog(f, A, b)

print(res)