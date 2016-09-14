import sys
import random
import time
import os

from change import *


def inputOutput():

	try:
		iFileName = sys.argv[2]
		inputFile = open(iFileName + ".txt", "r")
		# cannot read the file through an error
	except IOError:
		print("Could not open test file. Check to make sure the file is in the correct location and is readable.")
		exit(1)
	except IndexError:
		print("Usage: python main.py -t {file name}\n\tNote: Do not include the extension. It will be assumed to be a '.txt' file.\nThank you.")
		exit(1)

	# open the output file for writing using append
	outputFile = open(iFileName + "change.txt", "w+")

	# fileArray = inputFile.read()

	for m in range(1, 4):
		inputFile = open(iFileName + ".txt", "r")

		if m == 1:
			outputFile.write("Algorithm changedp:" + "\n")
		if m == 2:
			outputFile.write("Algorithm changegreedy:" + "\n")
		if m == 3:
			outputFile.write("Algorithm changeslow:" + "\n")

		while True:
			line1 = inputFile.readline()
			line2 = inputFile.readline()
			if not line2:
				break

			coinList = eval(line1)
			coinAmount = eval(line2)

			results = coinTiming(coinList, coinAmount, m)

			outputFile.write(str(results['denoms']) + "\n" + str(results['minCoins']) + "\n")

	inputFile.close()
	outputFile.close()


def problems():

	try:
		oFileName = sys.argv[2]
		# cannot read the file through an error
	except IndexError:
		print("Usage: python main.py -a {file name}\n\tNote: Do not include the extension. It will be assumed to be a '.txt' file.\nThank you.")
		exit(1)

	outputFile = open(oFileName + "results.txt", "w+")

	problem_4 = [1, 5, 10, 25, 50]
	problem_5a = [1, 2, 6, 12, 24, 48, 60]
	problem_5b = [1, 6, 13, 37, 150]
	problem_6 = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
	problem_8 = [[1],
				[1, 2],
				[1, 2, 3],
				[1, 2, 3, 5],
				[1, 2, 3, 5, 7],
				[1, 2, 3, 5, 7, 11],
				[1, 2, 3, 5, 7, 11, 13],
				[1, 2, 3, 5, 7, 11, 13, 17],
				[1, 2, 3, 5, 7, 11, 13, 17, 19],
				[1, 2, 3, 5, 7, 11, 13, 17, 19, 23]]
	problem_9 = [[1, 2, 4, 8, 16, 256],
				[1, 3, 9, 27, 729]]

	startVal4 = 2010
	endVal4 = 2200
	inc4 = 5

	startVal5 = 10000
	endVal5 = 10100
	inc5 = 1

	startVal9 = 100000
	endVal9 = 101000
	inc9 = 10

	startVal6 = 2000
	endVal6 = 2200
	inc6 = 1

	slowStart = 1
	slowEnd = 28
	slowInc = 1

	primeStart = 10000019  # arbitrarily large prime number
	primeStartSlow = 23

	# runs changegreedy and changedp over range of 2010 to 2200
	# increments by 5 each iteration

	outputFile.write("\n" + "Problem 4: dp and greedy" + "\n")
	obtainValues(outputFile, problem_4, startVal4, endVal4, inc4, 1)

	# # runs all 3 algorithms over a smaller range
	# # increments by 5 each iteration

	outputFile.write("\n" + "Problem 4: dp, greedy and slow" + "\n")
	obtainValues(outputFile, problem_4, slowStart, slowEnd, slowInc, 2)

	# # runs changegreedy and changedp over range of 10000 to 10100
	# # increments by 1 each iteration

	outputFile.write("\n" + "Problem 5a: dp and greedy" + "\n")
	obtainValues(outputFile, problem_5a, startVal5, endVal5, inc5, 1)

	# # runs all 3 algorithms over a smaller range
	# # increments by 1 each iteration

	outputFile.write("\n" + "Problem 5a: dp, greedy and slow" + "\n")
	obtainValues(outputFile, problem_5a, slowStart, slowEnd, slowInc, 2)

	# # runs changegreedy and changedp over range of 10000 to 10100
	# # increments by 1 each iteration

	outputFile.write("\n" + "Problem 5b: dp and greedy" + "\n")
	obtainValues(outputFile, problem_5b, startVal5, endVal5, inc5, 1)

	# # runs all 3 algorithms over a smaller range
	# # increments by 1 each iteration

	outputFile.write("\n" + "Problem 5b: dp, greedy and slow" + "\n")
	obtainValues(outputFile, problem_5b, slowStart, slowEnd, slowInc, 2)

	# # runs changegreedy and changedp over range of 2000 to 2200
	# # increments by 1 each iteration

	outputFile.write("\n" + "Problem 6: dp and greedy" + "\n")
	obtainValues(outputFile, problem_6, startVal6, endVal6, inc6, 1)

	# # runs all 3 algorithms over a smaller range
	# # increments by 1 each iteration

	outputFile.write("\n" + "Problem 6: dp, greedy and slow" + "\n")
	obtainValues(outputFile, problem_6, slowStart, slowEnd, slowInc, 2)

	# obtains timing data for different denom sizes
	for i in range(0, len(problem_8)):
		outputFile.write("\n" + "Problem 8b: dp, greedy; V = " + str(i) + "\n")
		obtainValues(outputFile, problem_8[i], primeStart, 0, 0, 3)
		outputFile.write("\n" + "Problem 8b: slow; V = " + str(i) + "\n")
		obtainValues(outputFile, problem_8[i], primeStartSlow, 0, 0, 4)

	for i in range(0, len(problem_9)):
		outputFile.write("\nProblem 9 using V = " + str(problem_9[i]) + "\n")
		obtainValues(outputFile, problem_9[i], startVal9, endVal9, inc9, 1)



	outputFile.close()


# function obtains minCoins and timing data depending on parameters
def obtainValues(outputFile, coinArray, startVal, endVal, inc, type):

	if type == 1:
		outputFile.write("\n" + "Algorithm changedp:" + "\n")

		for n in range(startVal, endVal + 1, inc):

			results = coinTiming(coinArray, n, 1)
			outputFile.write(str(n) + "\t" + str(results['minCoins']) + "\t" + str(results['execTime']) + "\n")

		outputFile.write("\n" + "Algorithm changegreedy:" + "\n")

		for n in range(startVal, endVal + 1, inc):

			results = coinTiming(coinArray, n, 2)
			outputFile.write(str(n) + "\t" + str(results['minCoins']) + "\t" + str(results['execTime']) + "\n")

	elif type == 2:
		outputFile.write("\n" + "Algorithm changedp:" + "\n")

		for n in range(startVal, endVal + 1, inc):

			results = coinTiming(coinArray, n, 1)
			outputFile.write(str(n) + "\t" + str(results['minCoins']) + "\t" + str(results['execTime']) + "\n")

		outputFile.write("\n" + "Algorithm changegreedy:" + "\n")

		for n in range(startVal, endVal + 1, inc):

			results = coinTiming(coinArray, n, 2)
			outputFile.write(str(n) + "\t" + str(results['minCoins']) + "\t" + str(results['execTime']) + "\n")

		outputFile.write("\n" + "Algorithm changeslow:" + "\n")
		for n in range(startVal, endVal + 1, inc):

			results = coinTiming(coinArray, n, 3)
			outputFile.write(str(n) + "\t" + str(results['minCoins']) + "\t" + str(results['execTime']) + "\n")

	elif type == 3:
			outputFile.write("\n" + "Algorithm changegreedy:" + "\n")

			results = coinTiming(coinArray, startVal, 2)
			outputFile.write(str(startVal) + "\t" + str(results['minCoins']) + "\t" + str(results['execTime']) + "\n")

			outputFile.write("\n" + "Algorithm changedp:" + "\n")

			results = coinTiming(coinArray, startVal, 1)
			outputFile.write(str(startVal) + "\t" + str(results['minCoins']) + "\t" + str(results['execTime']) + "\n")

	elif type == 4:
		outputFile.write("\n" + "Algorithm changeslow:" + "\n")
		results = coinTiming(coinArray, startVal, 3)
		outputFile.write(str(startVal) + "\t" + str(results['minCoins']) + "\t" + str(results['execTime']) + "\n")


def coinTiming(d, total, type):

	# calls the Coins constructor on the denominations and total amount
	x = Coins(d, total)
	print("d: " + str(d) + ", total: "+ str(total))

	# calculates denominations, minimum coins and timing for each algorithm
	if type == 1:
		s_time = time.time()
		denoms, minCoins = x.changedp()
		e_time = time.time()

	elif type == 2:
		s_time = time.time()
		denoms, minCoins = x.changegreedy()
		e_time = time.time()

	elif type == 3:
		s_time = time.time()
		denoms, minCoins = x.changeslow()
		e_time = time.time()

	execTime = e_time - s_time

	return {'denoms': denoms, 'minCoins': minCoins, 'execTime': execTime}


try:
	if sys.argv[1] == "-t":
		inputOutput()

	elif sys.argv[1] == "-a":
		problems()

# handle some unwanted errors
# such as if the right options were not given
except IndexError:
	print("Usage: python main.py {-a|-t} (file name)\n\t-a\tIndicates that you would like to test the predefined problem sets." + ".\n\t-t\tIndicates you would like a test a set from a file using predefined format but user defined sets.\nNote: The data will be available in the file name you specified with the extension '.txt'. If you specified 'test' then the results would be in 'test.txt'. Example use: python main.py -t mytestdata\nThank you.")
	exit(1)
# or if the user presses CTRL+C to terminate the program early
except KeyboardInterrupt:
	print("\nProgram interrupted.\n")
	exit(1)
