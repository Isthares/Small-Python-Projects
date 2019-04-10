# File Name: powerDigitSum.py
# Author: Esther Heralta Espinosa
# Date: 04/08/19
# Description of the program: 21 ** 5 = 4084101 and the sum of its digits is 4 + 0 + 8 + 4 + 1 + 0 + 1 = 18.
#							  What is the sum of the digits of the number 21000?

def sumDigits(number):
	""" returns the sum of the digits of the given number """
	sumTotal = 0
	for digit in number:
		if digit != '0':
			sumTotal = sumTotal + int(digit)

	return sumTotal


def main():
	number = 21000
	exp = 5
	power = pow(number, exp)
	strPower = str(power)
	print("\n{0} to the power of {1} is: {2}".format(number, exp, power))
	print("The sum of the digit of {0} is: {1}\n".format(power, sumDigits(strPower)))

if __name__ == "__main__":
	main()
