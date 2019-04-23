"""
File Name: 1000-digitFibonacciNumber.py
Author: Esther Heralta Espinosa
Date: 04/22/19
Description of the program: The Fibonacci sequence is defined by the recurrence relation:

			     Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
			     Hence the first 12 terms will be:
			     
			     F1 = 1
			     F2 = 1
			     F3 = 2
			     F4 = 3
			     F5 = 5
			     F6 = 8
			     F7 = 13
			     F8 = 21
			     F9 = 34
			     F10 = 55
			     F11 = 89
			     F12 = 144
			     The 12th term, F12, is the first term to contain three digits.
			     
			     What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

"""

ONE_THOUSAND = 1000


def getFibonacciDigits(fiboNumber):
	""" returns the number of digits that a given Fibonacci term contains 
		example: fiboNumber = 55, returns 2 digits
	"""
	return len(str(fiboNumber))


def fibonacci(number):
	""" returns the fibonacci number of the given number """
	""" by starting with 1 and 2"""
	if (number == 1) or (number == 2): #fibonacci(1) = 1 and fibonacci(2) = 2
		return (1)
	else:
		return (fibonacci(number - 1) + fibonacci(number - 2))


def main():
	digits = 0
	number = 1

	while digits != ONE_THOUSAND:
		fiboNumber = fibonacci(number)
		digits = getFibonacciDigits(fiboNumber)
		number += 1

	print("\nWhat is the index of the first term in the Fibonacci sequence to contain 1000 digits? {0} \n".format(number - 1))


if __name__ == "__main__":
	main()

