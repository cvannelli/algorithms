# Function returns the length of the palindrome within a string
def palindrome(string):
	# length of the string
	n = len(string)

	# creates a reversed version of the input string
	reverseString = string[::-1]

	# creates a matrix to store length values in
	L = [[0 for x in range(n + 1)] for x in range(n + 1)]

	for i in range(n + 1):			# for-loop iterates from 0 to n

		for j in range(n + 1):		# for-loop iterates from 0 to n

			if i == 0 or j == 0:
				L[i][j] = 0			# sets all table values to 0 when i or j are zero

			elif string[i - 1] == reverseString[j - 1]:
				L[i][j] = L[i - 1][j - 1] + 1

			else:
				L[i][j] = max(L[i - 1][j], L[i][j - 1])

	return L[n][n]

string = ['A', 'C', 'G', 'T', 'G', 'T', 'C', 'A', 'A', 'A', 'A', 'T', 'C', 'G']

print(palindrome(string))
