# File Name: largestProductInAGrid.py
# Author: Esther Heralta Espinosa
# Date: 04/06/19
# Description of the program: We have a 20 x 20 grid of numbers
#			      What is the greatest product of four adjacent numbers in the same direction 
#			      (up, down, left, right, or diagonally) in the 20 x 20 grid?

MAX_ADJACENT_NUMBERS = 4

def multAdjacentNumbers (arrayNumbers, index):
	""" arrayNumbers: [8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8] 
		index = 0 ==> num1 = 8, num2 = 2, num3 = 22, num4 = 97
		index = 2 ==> num1 = 22, num2 = 97, num3 = 38, num4 = 15
		index: index of the array
		return the product of four adjacent numbers
	"""
	num1 = arrayNumbers[index]
	num2 = arrayNumbers[index + 1]
	num3 = arrayNumbers[index + 2]
	num4 = arrayNumbers[index + 3]
	return num1 * num2 * num3 * num4


def greatestProductFromLeftToRight(grid):
	""" returns the greatest product of four adjacent numbers from left to right """
	greatestProduct = 1
	for array in grid:
		for index in range(0, len(array) - (MAX_ADJACENT_NUMBERS - 1)):
			resultat = multAdjacentNumbers(array, index)
			#print("resultat: {0}".format(resultat))
			if greatestProduct < resultat:
				greatestProduct = resultat

	return greatestProduct

def greatestProductFromRightToLeft(grid):
	""" returns the greatest product of four adjacent numbers from right to left 
		array = [8, 2, 22]				reversedArray = [22, 2, 8]		
	"""
	greatestProduct = 1
	for array in grid:
		reversedArray = list(reversed(array)) #reversing the array so I can you use a for from left to right
		#print(reversedArray)
		for index in range(0, len(reversedArray) - (MAX_ADJACENT_NUMBERS - 1)):
			resultat = multAdjacentNumbers(reversedArray, index)
			#print("resultat: {0}".format(resultat))
			if greatestProduct < resultat:
				greatestProduct = resultat
	
	return greatestProduct


def createGridFromUpToDown(oldGrid):
	""" returns a new grid of arrays from up to down 
		grid = [					newGrid = [
			[8, 2, 22], 				   [8, 7, 15],
		        [7, 27, 53],				   [2, 27, 10],
		        [15, 10, 28] 				   [22, 53, 28]
		        ]							   ]
	"""
	newGrid = []
	insertIndex = 0
	for row in range (0, len(oldGrid)):
		newArray = []
		for array in oldGrid:
			#print(array[insertIndex])
			newArray.append(array[insertIndex])
			#print(newArray)
		
		newGrid.append(newArray)
		insertIndex += 1

	return newGrid


def greatestProductFromUpToDown(grid):
	""" returns the greatest product of four adjacent numbers from up to down """
	newGrid = createGridFromUpToDown(grid)
	#print(newGrid)
	greatestProduct = greatestProductFromLeftToRight(newGrid)
	return greatestProduct


def greatestProductFromDownToUp(grid):
	""" returns the greatest product of four adjacent numbers from down to up """
	newGrid = createGridFromUpToDown(grid)
	#print(newGrid)
	#print("\n")
	greatestProduct = greatestProductFromRightToLeft(newGrid)
	return greatestProduct


def get_diagonal(grid, index):
	""" gets a diagonal """
	ret = []

	for row in grid:
		#print("index: {0}, row: {1}".format(index, row))
		if index < 0:
			index += 1
			continue

		if index >= len(row):
			index += 1
			continue

		ret.append(row[index])
		#print("index: {0}, ret: {1}".format(index, ret))
		index += 1

	return ret


def createGridDiagonal(oldGrid):
	""" returns a grid of diagonals """
	""" returns a new grid of arrays from diagonals 
		grid = [					newGrid = [
			[8, 2, 22], 				   	[8, 27, 28],
		        [7, 27, 53],				   	[2, 53],
		        [15, 10, 28] 				   	[22],
			]				   	   	[7, 10],
								   	[15]
								   	]
	"""
	#oldGrid = [[8, 2, 22],[7, 27, 53],[15, 10, 28]]
	newGrid = []

	# for index in range(-2, 3):
	# 	diagonal = get_diagonal(oldGrid, index)
	# 	newGrid.append(diagonal)
	# print(newGrid)
	# print('Diagonal -3: {0}'.format(get_diagonal(oldGrid, -3)))
	# print('Diagonal -2: {0}'.format(get_diagonal(oldGrid, -2)))
	# print('Diagonal -1: {0}'.format(get_diagonal(oldGrid, -1)))
	# print('Diagonal  0: {0}'.format(get_diagonal(oldGrid,  0)))
	# print('Diagonal  1: {0}'.format(get_diagonal(oldGrid,  1)))
	# print('Diagonal  2: {0}'.format(get_diagonal(oldGrid,  2)))
	# print('Diagonal  3: {0}'.format(get_diagonal(oldGrid,  3)))

	for index in range(-(len(oldGrid) - 1), len(oldGrid)):
		diagonal = get_diagonal(oldGrid, index)
		if len(diagonal) >= MAX_ADJACENT_NUMBERS: #do not append array with len < 4
			newGrid.append(diagonal)
	
	return newGrid

def greatestProductFromDiagonal(oldGrid):
	""" returns the greatest product of four adjacent numbers from diagonals """
	newGrid = createGridDiagonal(oldGrid)
	#print(newGrid)
	greatestProduct = greatestProductFromLeftToRight(newGrid)
	return greatestProduct


def main():
	#20 x 20 grid of numbers
	grid = [
		[8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
    		[49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
    		[81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
    		[52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
    		[22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
    		[24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
    		[32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
    		[67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
    		[24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
    		[21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],
    		[78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
    		[16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
    		[86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
    		[19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
    		[4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
    		[88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
    		[4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
    		[20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
    		[20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
    		[1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]
    ]
	
	print("\nThe greatest product of {0} adjacent number from left to right is: {1}\n".format(MAX_ADJACENT_NUMBERS, greatestProductFromLeftToRight(grid)))
	print("The greatest product of {0} adjacent number from right to left is: {1}\n".format(MAX_ADJACENT_NUMBERS,greatestProductFromRightToLeft(grid)))
	print("The greatest product of {0} adjacent number from up to down is: {1}\n".format(MAX_ADJACENT_NUMBERS,greatestProductFromUpToDown(grid)))
	print("The greatest product of {0} adjacent number from down to up is: {1}\n".format(MAX_ADJACENT_NUMBERS,greatestProductFromDownToUp(grid)))
	print("The greatest product of {0} adjacent number from diagonals is: {1}\n".format(MAX_ADJACENT_NUMBERS,greatestProductFromDiagonal(grid)))

	
if __name__ == "__main__":
	main()
	
