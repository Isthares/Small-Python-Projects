# File Name: largestPalindromeProduct.py
# Author: Esther Heralta Espinosa
# Date: 04/05/19
# Description of the program: A palindromic number reads the same both ways.
#			      The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
#			      Find the largest palindrome made from the product of two 3-digit numbers.
 
def isPalindrome(number):
	""" returns true if the given number is palindrome, otherwise false """
	strNumber = str(number) #convert to a string
	start = 0
	end = len(strNumber) - 1

	while start != (len(strNumber) / 2):
		if strNumber[start] == strNumber[end]:
			start = start + 1
			end = end - 1
		else:
			return False
	return True



def main():
	#list that contains all positive integers numbers of three digits
	threeDigitList = [x for x in range (100, 1000)]
	#twoDigitList = [x for x in range (10, 100)]
	#print(twoDigitList)

	palindromeList = []
	for i in threeDigitList:
		for j in threeDigitList:
			num = i * j
			if isPalindrome(num):
				palindromeList.append(num)

	#print("\nList of palindromes: {0}".format(palindromeList))
	#print("\nThe largest palindrome made from the product of two 2-digit numbers is: {0}\n".format(max(palindromeList)))
	print("\nThe largest palindrome made from the product of two 3-digit numbers is: {0}\n".format(max(palindromeList)))


if __name__ == "__main__":
	main()
