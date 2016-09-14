from tspFunctions import *


def main(argc, argv):
	# Get filename from command line
	# Reference: stackoverflow http://stackoverflow.com/questions/8201955/
	filename = None
	filename = sys.argv[1]

	cityList = readinstance(filename)

	# Open input file and parse into an array of vertices and X&Y coords
	inputFD = open(filename)
	vertices = {}

	# loop through lines in input file and add to vertices
	for l in inputFD:
		procLine = l.strip("\n\r").split()
		vertices[int(procLine[0])] = (int(procLine[1]), int(procLine[2]))

	inputFD.close()

	# start execution time tracking
	start = time.time()

	if (cityList.cityCount() > 1000):

		# Find a SINGLE shortest path
		# NOTE: This is to speed up the process with large inputs
		# but will likely find a much less optimal path compared to
		# our tsp2Greedy(original) method, as it is not finding the
		# optimal path considering multiple starting vertices
		# call getgreedyTSP to calculate the path
		tsp = getgreedyTSP(vertices, 0)

	else:

		# create a complete graph of the vertices
		graph = Graph(cityList)

		# obtain a list of the odd vertices from the MST
		oddVerts = getOdds(graph.MST())

		# creates a multigraph with even vertices
		match = PerfectMatch(oddVerts, graph.returnGraph(), graph.MST())
		multiGraph = match.edges()

		# calculates the euler circuit of the multigraph
		path = Euler(multiGraph)
		eul = EulerCircuit(path, cityList)

		# converts the euler circuit to a hamilton circuit
		tsp = eul.hamilton()

	# end execution time tracking
	end = time.time()
	exTime = end - start

	print("Execution Time: %d") % (exTime)

	# Verify that time is within time limit
	if exTime <= 180:
		print("Within Time Limit(180): TRUE")
	else:
		print("Within TIme Limit(180): FALSE")

	# Store results in output file
	outputFD = open(filename + ".tour", "w")
	outputFD.writelines([str(tsp[1]), "\n"])

	for vertex in tsp[0]:
		outputFD.writelines([str(vertex), "\n"])

	outputFD.close()


if __name__ == "__main__":
	main(len(sys.argv), sys.argv)