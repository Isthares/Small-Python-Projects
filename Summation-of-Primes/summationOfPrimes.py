# File Name: summationOfPrimes.py
# Author: Esther Heralta Espinosa
# Date: 04/06/19
# Description of the program: The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#							  Find the sum of all the primes below 1000.

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
	primeNumbers = []
	for num in range (1, MAX + 1):
		if isPrime(num):
			primeNumbers.append(num)
	print("Sum of all the prime numbers below {0}: {1}".format(MAX, sum(primeNumbers)))


if __name__ == "__main__":
	main()
