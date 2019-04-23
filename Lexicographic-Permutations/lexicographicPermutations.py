# File Name: lexicographicPermutations.py
# Author: Esther Heralta Espinosa
# Date: 04/22/19
# Description of the program: A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation 
#			      of the digits 1, 2, 3 and 4. 
#		              If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
#			      The lexicographic permutations of 0, 1 and 2 are:

#					012   021   102   120   201   210

#			       What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

from itertools import permutations 

def main():
	#returns a list of tuple that contains all possible per muations of digits 0, 1, ..., 9
	perm = permutations([0,1, 2, 3, 4, 5, 6, 7, 8, 9])

	for index, aTuple in enumerate(perm):
		if index == 1000000:
			print("\nWhat is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?  {0} \n".format(aTuple))

if __name__ == "__main__":
	main()
