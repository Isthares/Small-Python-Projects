# File Name: non-abundantSums.py
# Author: Esther Heralta Espinosa
# Date: 04/21/19
# Description of the program: A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
#			      For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, 
#			      which means that 28 is a perfect number.

#			      A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant 		
#			      if this sum exceeds n.

#			      As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written 
#			      as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers 
#			      greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot 
#			      be reduced any further by analysis even though it is known that the greatest number that cannot be 
#			      expressed as the sum of two abundant numbers is less than this limit.

#			      Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.	


LIMIT = 28123


def getDivisorsOfNumber(number):
	""" returns a list with the divisors of a the given number
		7: 1
		8: 1, 2, 4
	"""
	factorsList = [1]

	for divisor in range (2, number):
		if (number % divisor) == 0: #it is divisible
			factorsList.append(divisor)

	#factorsList.sort() #ordering the list

	return factorsList


#def isNumberPerfect(aNumber):
#	""" returns true if a number is perfect (the sum of the number divisors is equal to the number)
#	    example: number = 28 >>> 1 + 2 + 4 + 7 + 14 = 28, 28 is perfect number because 28 = 28
#	"""
#	divisorsList = getDivisorsOfNumber(aNumber)
#	if sum(divisorsList) == aNumber:
#		return True
#	else:
#		return False


#def isNumberDeficient(aNumber):
#	""" returns true if a number is deficient (the sum of the number divisors is less than the number)
#	    example: number = 21 >>> 1 + 3 + 7 = 11, 21 is deficient number because 11 < 21
#	"""
#	divisorsList = getDivisorsOfNumber(aNumber)
#	if sum(divisorsList) < aNumber:
#		return True
#	else:
#		return False


def isNumberAbundant(aNumber):
	""" returns true if a number is abundant (the sum of the number divisors is greater than the number)
	    example: number = 12 >>> 1 + 2 + 3 + 4 + 6 = 16, 12 is abundant number because 16 > 12
	"""
	divisorsList = getDivisorsOfNumber(aNumber)
	if sum(divisorsList) > aNumber:
		return True
	else:
		return False


def getListOfAbundantNumbers():
	""" returns a list that contains abundant numbers that are less than LIMIT (28123) """
	abundantNumbersList = []
	for num in range(1, LIMIT + 1):
		if isNumberAbundant(num):
			abundantNumbersList.append(num)

	return abundantNumbersList


def getListNumbersCanBeWritenAsSumOfTwoAbundantNumber(aListAbundantNumbers):
	""" returns a list with the numbers that can be writen as the sum of two abundant numbers """
	numbersList = []
	currentIndex = 0
	currentPosition = 0
	aSum = 0

	while currentIndex < len(aListAbundantNumbers):
		currentPosition = currentIndex

		while currentPosition < len(aListAbundantNumbers):
			aSum = aListAbundantNumbers[currentIndex] + aListAbundantNumbers[currentPosition]
			if aSum not in numbersList:
				numbersList.append(aSum)
			currentPosition += 1

		currentIndex += 1

	return numbersList


def getListNumbersCannotBeWritenAsSumOfTwoAbundantNumbers(aListSumTwoAbundantNumbers):
	""" given a list that contains numbers that can be writen as the sum of two abundant numbers 
	    the function returns a list with the numbers that cannot be writen as the sum of two abundant numbers """
	numbersList = []

	for num in range (1, LIMIT + 1):
		if num not in aListSumTwoAbundantNumbers:
			numbersList.append(num)

	return numbersList


def main():
	aList = getListOfAbundantNumbers()
	#print(aList)
	#print("\n")
	aList2 = getListNumbersCanBeWritenAsSumOfTwoAbundantNumber(aList)
	#print(aList2)
	#print("\n")
	aList3 = getListNumbersCannotBeWritenAsSumOfTwoAbundantNumbers(aList2)
	#print(aList3)
	print("\n")
	print("Sum of all positive integers that cannot be written as the sum of two abundant numbers: {0} \n".format(sum(aList3)))

if __name__ == "__main__":
	main()	
