# File Name: screen.py
# Author: Esther Heralta Espinosa
# Date: 02/20/19
# Description of the program: Conversion Calculator

# This class contains functions that are related to displaying something on the screen
# or asking the user to enter some kind of data

# ---------------------------------- Libraries ----------------------------------
import validate #module
# -------------------------------------------------------------------------------

class Screen():
	""" displaying something on the screen or gathering data from the user """


	# -------------------------------- Main Menu Functions ---------------------------------
	#display the main menu on the screen
	def mainMenu(self):
	    """ Display main menu on the screen """
	    print("\n")
	    print("	----------- CONVERSION CALCULATOR MENU ----------- \n")
	    print("		1. Temperature		")
	    print("		2. Weight			")
	    print("		3. Time				")
	    print("		4. Exit				")
	    #print("\n")
	    print("	-------------------------------------------------- ")

	def getMenuOption(self):
		""" prompt the user to choose an option of the main menu """
		print("\n")
		option = int(input("	Enter an option: "))
		#print(option, type(option))
		return (option)

	def displayInvalidOptionMessage(self):
		""" display a message telling the user that the option entered is not valid """
		print("\n")
		print("	Invalid choice. Please, choose a valid one.")

	def getValidMainMenuOption(self, optionChosen):
		vd = validate.ValidateData()

		""" prompts the user for an option and checks whether is valid or not """
		while (vd.isValidMainMenuOption(optionChosen) == False):
			self.displayInvalidOptionMessage()
			self.mainMenu() #display the main menu on the screen
			optionChosen = self.getMenuOption()

	# --------------------------------------------------------------------------------------

	# ------------------------------------ Exit Option -------------------------------------
	def exitMessage(self):
		""" display exit message """
		print("\n")
		print("	You have exit the Conversion Calculator.\n")
	# --------------------------------------------------------------------------------------

	# -------------------------------- Temperature Options ----------------------------------
	def temperatureMenu(self):
		""" Display temperatura menu on the screen """
		print("\n")
		print("	---------------- TEMPERATURE MENU --------------- \n")
		print("		1. Convert Celsius to Fahrenheit		")
		print("		2. Convert Celsius to Kelvin			")
		print("		3. Convert Fahrenheit to Celsius	 	")
		print("		4. Convert Fahrenheit to Kelvin	 		")
		print("		5. Convert Kelvin to Celsius	 		")
		print("		6. Convert Kelvin to Fahrenheit		 	")
		print("		7. Exit	 								")
		#print("\n")
		print("	-------------------------------------------------- ")


	def getValidTemperatureMenuOption(self, optionChosen):
		""" prompts the user for an option and checks whether is valid or not """
		vd = validate.ValidateData()

		while (vd.isValidSubMenuOption(optionChosen) == False):
			self.displayInvalidOptionMessage()
			self.temperatureMenu() #display the temperature menu on the screen
			optionChosen = self.getMenuOption()

	def getValueToConvert(self):
		""" prompt the user to enter the value that is going to be converted """
		#print("\n")
		option = float(input("	Enter the value to convert: "))
		return (option)

	def displayTemperatureConversionMessage(self, optionChosen, dataToConvert, dataConverted):
		""" display a message telling the user the result of the conversion chosen """

		print("\n")
		if (optionChosen == 1):
			print("	{0} C = {1:.2f} F ".format(dataToConvert, dataConverted))
		elif (optionChosen == 2):
			print("	{0} C = {1:.2f} K ".format(dataToConvert, dataConverted))
		elif (optionChosen == 3):
			print("	{0} F = {1:.2f} C ".format(dataToConvert, dataConverted))
		elif (optionChosen == 4):
			print("	{0} F = {1:.2f} K ".format(dataToConvert, dataConverted))
		elif (optionChosen == 5):
			print("	{0} K = {1:.2f} C ".format(dataToConvert, dataConverted))
		elif (optionChosen == 6):
			print("	{0} K = {1:.2f} F ".format(dataToConvert, dataConverted))

	# --------------------------------------------------------------------------------------

	# ---------------------------------- Weight Options ------------------------------------
	def weightMenu(self):
		""" Display weight menu on the screen """
		print("\n")
		print("	------------------- WEIGHT MENU ----------------- \n")
		print("		1. Convert Gram to Ounce			")
		print("		2. Convert Gram to Pound			")
		print("		3. Convert Ounce to Gram		 	")
		print("		4. Convert Ounce to Pound	 		")
		print("		5. Convert Pound to Gram	 		")
		print("		6. Convert Pound to Ounce		 	")
		print("		7. Exit	 							")
		#print("\n")
		print("	-------------------------------------------------- ")

	def getValidWeightMenuOption(self, optionChosen):
		""" prompts the user for an option and checks whether is valid or not """
		vd = validate.ValidateData()

		while (vd.isValidSubMenuOption(optionChosen) == False):
			self.displayInvalidOptionMessage()
			self.weightMenu() #display the weight menu on the screen
			optionChosen = self.getMenuOption()

	def displayWeightConversionMessage(self, optionChosen, dataToConvert, dataConverted):
		""" display a message telling the user the result of the conversion chosen """

		print("\n")
		if (optionChosen == 1):
			print("	{0} grams = {1:.3f} ounces ".format(dataToConvert, dataConverted))
		elif (optionChosen == 2):
			print("	{0} grams = {1:.3f} pounds ".format(dataToConvert, dataConverted))
		elif (optionChosen == 3):
			print("	{0} ounces = {1:.3f} grams ".format(dataToConvert, dataConverted))
		elif (optionChosen == 4):
			print("	{0} ounces = {1:.3f} pounds ".format(dataToConvert, dataConverted))
		elif (optionChosen == 5):
			print("	{0} pounds = {1:.3f} grams ".format(dataToConvert, dataConverted))
		elif (optionChosen == 6):
			print("	{0} pounds = {1:.3f} ounces ".format(dataToConvert, dataConverted))
	# --------------------------------------------------------------------------------------

	# ----------------------------------- Time Options -------------------------------------
	def timeMenu(self):
		""" Display time menu on the screen """
		print("\n")
		print("	-------------------- TIME MENU ------------------- \n")
		print("		1. Convert hours to minutes			")
		print("		2. Convert hours to seconds			")
		print("		3. Convert minutes to hours		 	")
		print("		4. Convert minutes to seconds	 	")
		print("		5. Convert seconds to hours		 	")
		print("		6. Convert seconds to minutes	 	")
		print("		7. Convert days to hours	 		")
		print("		8. Convert days to minutes		 	")
		print("		9. Convert days to seconds	 		")
		print("		0. Exit	 							")
		#print("\n")
		print("	-------------------------------------------------- ")

	def getValidTimeMenuOption(self, optionChosen):
		""" prompts the user for an option and checks whether is valid or not """
		vd = validate.ValidateData()

		while (vd.isValidTimeMenuOption(optionChosen) == False):
			self.displayInvalidOptionMessage()
			self.timeMenu() #display the time menu on the screen
			optionChosen = self.getMenuOption()

	def displayTimeConversionMessage(self, optionChosen, dataToConvert, dataConverted):
		""" display a message telling the user the result of the conversion chosen """

		print("\n")
		if (optionChosen == 1):
			print("	{0} hours = {1:.3f} minutes ".format(dataToConvert, dataConverted))
		elif (optionChosen == 2):
			print("	{0} hours = {1:.3f} seconds ".format(dataToConvert, dataConverted))
		elif (optionChosen == 3):
			print("	{0} minutes = {1:.3f} hours ".format(dataToConvert, dataConverted))
		elif (optionChosen == 4):
			print("	{0} minutes = {1:.3f} seconds ".format(dataToConvert, dataConverted))
		elif (optionChosen == 5):
			print("	{0} seconds = {1:.5f} hours ".format(dataToConvert, dataConverted))
		elif (optionChosen == 6):
			print("	{0} seconds = {1:.5f} minutes ".format(dataToConvert, dataConverted))
		elif (optionChosen == 7):
			print("	{0} days = {1:.3f} hours ".format(dataToConvert, dataConverted))
		elif (optionChosen == 8):
			print("	{0} days = {1:.3f} minutes ".format(dataToConvert, dataConverted))
		elif (optionChosen == 9):
			print("	{0} days = {1:.3f} seconds ".format(dataToConvert, dataConverted))
	# --------------------------------------------------------------------------------------
