# File Name: validate.py
# Author: Esther Heralta Espinosa
# Date: 02/20/19
# Description of the program: Conversion Calculator

# ---------------------------------- Libraries ----------------------------------
import convert #module
# -------------------------------------------------------------------------------


class ValidateData():
	""" This class validates and treats data entered by the user """
	
	def isValidMainMenuOption(self, optionChosen):
		""" checks if wheter the option entered by the user is correct 
		    - if correct: return true
		    - else: return false """

		#print(optionChosen, type(optionChosen))
		if ((optionChosen == 1) | (optionChosen == 2) | (optionChosen == 3) | (optionChosen == 4)):
			return (True)
		else:
			return (False) 

	def isValidSubMenuOption(self, optionChosen):
		""" checks if wheter the option entered by the user is correct 
		    - if correct: return true
		    - else: return false """
		if ((optionChosen == 1) | (optionChosen == 2) | (optionChosen == 3) | (optionChosen == 4) | (optionChosen == 5) 
			| (optionChosen == 6) | (optionChosen == 7)):
			return (True)
		else:
			return (False) 

	def optionTreatmentTemperature(self, valueToConvert, optionChosen):
		""" depending of the option chosen by the user, the program will execute a conversion or exit the temperature menu """
		cTemp = convert.ConvertTo()

		if (optionChosen == 1):
			return (cTemp.convertCelsiusToFahrenheit(valueToConvert)) 
		elif (optionChosen == 2):
			return (cTemp.convertCelsiusToKelvin(valueToConvert))
		elif (optionChosen == 3):
			return (cTemp.convertFahrenheitToCelsius(valueToConvert))
		elif (optionChosen == 4):
			return (cTemp.convertFahrenheitToKelvin(valueToConvert))
		elif (optionChosen == 5):
			return (cTemp.convertKelvinToCelsius(valueToConvert))
		elif (optionChosen == 6):
			return (cTemp.convertKelvinToFahrenheit(valueToConvert))
		
	def optionTreatmentWeight(self, valueToConvert, optionChosen):
		""" depending of the option chosen by the user, the program will execute a conversion or exit the weight menu """
		cWeight = convert.ConvertTo()

		if (optionChosen == 1):
			return (cWeight.convertGramToOunce(valueToConvert)) 
		elif (optionChosen == 2):
			return (cWeight.convertGramToPound(valueToConvert))
		elif (optionChosen == 3):
			return (cWeight.convertOunceToGram(valueToConvert))
		elif (optionChosen == 4):
			return (cWeight.convertOunceToPound(valueToConvert))
		elif (optionChosen == 5):
			return (cWeight.convertPoundToGram(valueToConvert))
		elif (optionChosen == 6):
			return (cWeight.convertPoundToOunce(valueToConvert))

	def isValidTimeMenuOption(self, optionChosen):
		""" checks if wheter the option entered by the user is correct 
		    - if correct: return true
		    - else: return false """
		if ((optionChosen == 1) | (optionChosen == 2) | (optionChosen == 3) | (optionChosen == 4) | (optionChosen == 5) 
			| (optionChosen == 6) | (optionChosen == 7) | (optionChosen == 8) | (optionChosen == 9) | (optionChosen == 0)):
			return (True)
		else:
			return (False) 

	def optionTreatmentTime(self, valueToConvert, optionChosen):
		""" depending of the option chosen by the user, the program will execute a conversion or exit the time menu """
		cTime = convert.ConvertTo()

		if (optionChosen == 1):
			return (cTime.convertHoursToMinutes(valueToConvert)) 
		elif (optionChosen == 2):
			return (cTime.convertHoursToSeconds(valueToConvert))
		elif (optionChosen == 3):
			return (cTime.convertMinutesToHours(valueToConvert))
		elif (optionChosen == 4):
			return (cTime.convertMinutesToSeconds(valueToConvert))
		elif (optionChosen == 5):
			return (cTime.convertSecondsToHours(valueToConvert))
		elif (optionChosen == 6):
			return (cTime.convertSecondsToMinutes(valueToConvert))
		elif (optionChosen == 7):
			return (cTime.convertDaysToHours(valueToConvert))
		elif (optionChosen == 8):
			return (cTime.convertDaysToMinutes(valueToConvert))
		elif (optionChosen == 9):
			return (cTime.convertDaysToSeconds(valueToConvert))


