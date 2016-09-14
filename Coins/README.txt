Include main.py, change.py

Usage: python main.py {-a|-t} (file name)
	-a	Indicates that you would like to test the predefined problem sets..
	-t	Indicates you would like a test a set from a file using predefined format but user defined sets.
Note: The data will be available in the file name you specified with the extension '.txt'. If you specified 'test' then the results would be in 'test.txt'. Example use: python main.py -t mytestdata

This will read from the specified file and output to  the specified 'file + change.txt'. If the filename specified was mytestdata then the contents would be contained in 'mytestdatachange.txt'.
The other option, -a,  is our experimental test cases, which are hard coded arrays we created and tested our algorithms against and the results would be found in the specified 'file + results.txt', similar to the above format.

When using a file for the -t condition, please be aware that this runs all three tests: slow, greedy and dynamic programming. Be careful when your total/amount is greater than 28, as that will cause excessively long run times.

The output format is as follows

Algorithm (algorithm name):
[subarray]
minimum coins


