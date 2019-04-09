# File Name: primeNumber.py
# Author: Esther Heralta Espinosa
# Date: 04/05/19
# Description of the program: By listing the first six prime numbers: 
#			      2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#			      What is the 1000 prime number?

MAX = 1000

def isPrime(number):
	""" returns true if the given number is prime """
	""" prime number: number > 1, and divisible only by itself or 1 """

	if number > 1:
		#check if the number is prime
		for num in range (2, number):
			#print ("number: {0}, num: {1}".format(number, num))
			if (number % num) == 0:
				#it is not prime
				return False
		return True
	else:
		return False


def main():
	exit = False
	countPrimeNumbers = 0
	number = 2

	while not exit:
		if isPrime(number):
			countPrimeNumbers += 1
		if countPrimeNumbers == MAX:
			exit = True
		else:
			number += 1

	print("\nThe {0} prime number is: {1}\n".format(MAX, number))


if __name__ == "__main__":
	main()
