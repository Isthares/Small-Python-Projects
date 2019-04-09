# File Name: smallestMultiple.py
# Author: Esther Heralta Espinosa
# Date: 04/05/19
# Description of the program: 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#							  What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 15?

MAX = 15


def main():
	numbers = [num for num in range(2, MAX + 1)]
	smallestNumber = MAX + 1 #initial smallest number that is divisible by all numbers from 1 to 20

	allNumbers = False
	while not allNumbers:
		for num in numbers:
			if (smallestNumber % num) != 0:
				smallestNumber = smallestNumber + 1
				break
			else:
				if num == MAX:
					allNumbers = True

	print("\nThe smallest number divisible by all of the numbers from 1 to {0}: {1}\n".format(MAX, smallestNumber))	



if __name__ == "__main__":
	main()
