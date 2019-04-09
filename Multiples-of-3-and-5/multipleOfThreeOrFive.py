# File Name: multipleOfThreeOrFive.py
# Author: Esther Heralta Espinosa
# Date: 04/05/19
# Description of the program: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
#							                The sum of these multiples is 23.
#							                Find the sum of all the multiples of 3 or 5 below 1000.

def isMultipleOfThree (number):
	""" returns whether a number is multiple or not of 3 """
	return (number % 3 == 0)

def isMultipleOfFive (number):
	""" returns whether a number is multiple or not of 5 """
	return (number % 5 == 0)

def main():
	#create a list of numbers from 1 to 1000
	numbers = [x for x in range(1, 1001)]
	
	multiples = []
	for number in numbers:
		if isMultipleOfThree(number) or isMultipleOfFive(number):
			multiples.append(number)
	
	print("\nSum of all multiples of 3 or 5 below 1000: {0}\n".format(sum(multiples)))

if __name__ == "__main__":
	main()
