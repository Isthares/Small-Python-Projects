# File Name: specialPythagoreanTriplet.py
# Author: Esther Heralta Espinosa
# Date: 04/06/19
# Description of the program: A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
#			      For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#			      There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#			      Find the product abc.

SUM = 1000

def main():
	# (a ** 2) + (b ** 2) = (c ** 2)
	# a + b + c = SUM

	# because a < b < c then:
	# 	c = SUM - a - b   and   c => 1 ... 1000
	#	b < c  and  b > a  ==>  b => 1 ... 999
	#   a < b  and  a < c  ==>  a => 1 ... 998

	for a in range(1, SUM - 1):
		for b in range (1, SUM):
			c = SUM - a - b
			if (a ** 2) + (b ** 2) == (c ** 2) and (a < b < c):
				print("a: {0}, b: {1}, and c: {2}".format(a, b, c))


if __name__ == "__main__":
	main()
