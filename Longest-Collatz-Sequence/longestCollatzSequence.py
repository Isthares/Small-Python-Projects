# File Name: longestCollatzSequence.py
# Author: Esther Heralta Espinosa
# Date: 04/08/19
# Description of the program: The following iterative sequence is defined for the set of positive integers:
#							  n >> n/2 (n is even)
#							  n >> 3n + 1 (n is odd)
#							  Using the rule above and starting with 13, we generate the following sequence:
#							  13 >> 40 >> 20 >> 10 >> 5 >> 16 >> 8 >> 4 >> 2 >> 1
#							  It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
#							  Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#							  Which starting number, under one million, produces the longest chain?

LIMIT = 999999

def generateSequence(number, sequenceList):
	""" returns a list with the sequence of the given number 
		if even: number -> number / 2
		if odd: (3 * number) + 1
	"""
	if number == 1:
		return sequenceList
	else:
		isEven = number % 2 == 0
		if isEven:
			number = number / 2
		else:
			number = (3 * number) + 1
		sequenceList.append(number)
		return generateSequence(number, sequenceList)



def main():
	# sequence = generateSequence(20, [20])
	# print(sequence)

	longestChain = []
	for num in range(LIMIT, 0, -1):
		sequence = generateSequence(num, [num])
		#print("current sequence: {0}".format(sequence))
		#print("current longest chain: {0}".format(longestChain))
		if len(longestChain) >= len(sequence):
			continue
		else: #len(longestChain) < len(sequence)
			longestChain = sequence

	print(longestChain)

if __name__ == "__main__":
	main()
