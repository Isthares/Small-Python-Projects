# File Name: sumSquareDifference.py
# Author: Esther Heralta Espinosa
# Date: 04/05/19
# Description of the program: The sum of the squares of the first ten natural numbers is: 12 + 22 + ... + 102 = 385
#							  The square of the sum of the first ten natural numbers is: (1 + 2 + ... + 10)2 = 552 = 3025
#							  Hence the difference between the sum of the squares of the first ten natural numbers 
#							  and the square of the sum is 3025 - 385 = 2640.
#							  Find the difference between the sum of the squares of the first one hundred natural numbers 
#						      and the square of the sum.

MAX = 100

def sumOfTheSquares(numbers):
	""" returns the sum of the squares of the first MAX natural numbers """ 
	squares = list(map(lambda x: x ** 2, numbers))
	#sum of the squares of the first MAX natural numbers
	return sum(squares)

def squareOfTheSum(numbers):
	""" returns the square of the sum of the first MAX natural numbers """
	addition = sum(numbers)
	return addition ** 2


def main():
	#squares of the first MAX natural numbers
	numbers = [x for x in range(1, MAX + 1)]
	sumSquares = sumOfTheSquares(numbers)
	squareSum = squareOfTheSum(numbers)
	print("\nThe sum of the squares of the first {0} natural numbers is: {1}".format(MAX, sumSquares))
	print("\nThe square of the sum of the first {1} natural numbers is: {1}".format(MAX, squareSum))
	print("\nThe difference between the sum of the squares of the first {0} natural numbers and the square of the sum is: {1}\n".format(MAX, squareSum - sumSquares))


if __name__ == "__main__":
	main()
