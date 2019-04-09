# File Name: largestPrimeFactor.py
# Author: Esther Heralta Espinosa
# Date: 04/05/19
# Description of the program: The prime factors of 13195 are 5, 7, 13 and 29.
#			      The largest prime factor of 13195 is 29.
#	                      What is the largest prime factor of a number entered by the user?

"""
2 x 3 = 6 --> 2 is a factor and 3 is a factor.
Prime factor: a factor that is a prime number.
In other words: any of the prime numbers that can be multiplied to give the original number.
Example: The prime factors of 15 are 3 and 5 --> because 3 * 5 = 15, and 3 and 5 are prime numbers
"""
	
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

def getPrimeFactors(number, primeNumbersList):
	""" returns a list that contains the prime factors of the given number """

	#find a suitable divisor for number : number % divisor == 0
	divisor = 2
	while (number % divisor) != 0:
		divisor = divisor + 1

	result = number / divisor

	if isPrime(divisor):
		if divisor not in primeNumbersList:
			primeNumbersList.append(divisor)

	if isPrime(result):
		if result not in primeNumbersList:
			primeNumbersList.append(result)
		return primeNumbersList
	else:
		return getPrimeFactors(result, primeNumbersList)



def main():
	number = int(input("\nEnter a number: "))

	if isPrime(number): #if the number entered is a prime number
		print("\nThe largest prime factor of the number '{0}' is {1}.".format(number, number))
		print("\n'{0}' is already a prime number\n".format(number))
	else:
		primeFactors = []
		primeFactors = getPrimeFactors(number, primeFactors)
		print("\nList of prime factors of {0}: {1}".format(number, primeFactors))
		print("\nThe largest prime factor of the number '{0}' is {1}. \n".format(number, max(primeFactors)))


if __name__ == "__main__":
	main()
