import time


def enumeration(A):
	s_time = time.time()

	maxSum = 0
	startIndex = stopIndex = 0

	for i in range(len(A)):

		for j in range(i, len(A)):

			currentSum = sum(A[i:j + 1])

			if currentSum > maxSum:
				maxSum = currentSum
				startIndex = i
				stopIndex = j + 1
	e_time = time.time()
	return {'subarray': A[startIndex:stopIndex], 'maxSum': maxSum, 'execTime': float(e_time - s_time)}


def betterEnumeration(A):
	s_time = time.time()

	maxSum = 0
	startIndex = stopIndex = 0

	for i in range(len(A)):
		currentSum = 0

		for j in range(i, len(A)):
			currentSum = currentSum + A[j]

			if currentSum > maxSum:
				maxSum = currentSum
				startIndex = i
				stopIndex = j + 1

	e_time = time.time()
	return {'subarray': A[startIndex:stopIndex], 'maxSum': maxSum, 'execTime': float(e_time - s_time)}


# EXAMPLE

array = [12, 12, 14, -88, -1, 45, 6, 8, -33, 2, 8, -9, -33, -8, -23, -77, -89, 1, 9, 10, 92, 87]

print(enumeration(array))
print(betterEnumeration(array))

