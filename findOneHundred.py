#https://www.reddit.com/r/dailyprogrammer/comments/69y21t/20170508_challenge_314_easy_concatenated_integers/

import sys
import itertools
commands = []
for line in sys.stdin:
	commands.append(line)

def findNumbers(list):
	for line in list:
		numbs = line.split()
		largest = 0
		smallest = 0
		for x in itertools.permutations(numbs):
			curr = 0
			sNum = ""
			for g in x:
				sNum += g
			curr = int(sNum)
			if curr > largest:
				largest = curr
			if curr < smallest or smallest == 0:
				smallest = curr
		print(smallest , largest)
		
findNumbers(commands)