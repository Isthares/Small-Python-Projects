# File Name: convert.py
# Author: Esther Heralta Espinosa
# Date: 02/20/19
# Description of the program: Conversion Calculator

#This class convert the data entered by the user to the chosen unit

class ConvertTo():
	""" This class convert the data entered by the user to the chosen unit """

	# ------------- Temperature Conversions -------------
	def convertCelsiusToFahrenheit (self, dataToConvert):
		""" converts celsius to fahrenheit """
		return ((dataToConvert * 9 / 5) + 32)

	def convertCelsiusToKelvin (self, dataToConvert):
		""" converts celsius to kelvin """
		return (dataToConvert + 273.15) 

	def convertKelvinToFahrenheit (self, dataToConvert):
		""" converts kelvin to fahrenheit """
		return ((dataToConvert - 273.15) * 9 / 5 + 32) 

	def convertKelvinToCelsius (self, dataToConvert):
		""" converts kelvin to celsius """
		return (dataToConvert - 273.15)

	def convertFahrenheitToCelsius (self, dataToConvert):
		""" converts fahrenheit to celsius """
		return ((dataToConvert - 32) * 5 / 9) 

	def convertFahrenheitToKelvin (self, dataToConvert):
		""" converts fahrenheit to kelvin """
		return ((dataToConvert - 32) * 5 / 9 + 273.15)
	# ---------------------------------------------------

	# ---------------- Weight Conversions ---------------
	def convertGramToOunce(self, dataToConvert):
		""" converts grams to ounces """
		return (dataToConvert / 28.35)

	def convertGramToPound(self, dataToConvert):
		""" converts grams to pounds """
		return (dataToConvert / 453.592)

	def convertOunceToGram(self, dataToConvert):
		""" converts ounces to grams """
		return (dataToConvert * 28.35)

	def convertOunceToPound(self, dataToConvert):
		""" converts ounces to pounds """
		return (dataToConvert / 16)

	def convertPoundToGram(self, dataToConvert):
		""" converts pounds to grams """
		return (dataToConvert * 453.592)

	def convertPoundToOunce(self, dataToConvert):
		""" converts pounds to ounces """
		return (dataToConvert * 16)
	# ---------------------------------------------------

	# ----------------- Time Conversions ----------------
	def convertHoursToMinutes(self, dataToConvert):
		""" converts hours to minutes """
		return (dataToConvert * 60)

	def convertHoursToSeconds(self, dataToConvert):
		""" converts hours to seconds """
		return (dataToConvert * 3600)

	def convertMinutesToHours(self, dataToConvert):
		""" converts minutes to hours """
		return (dataToConvert / 60)

	def convertMinutesToSeconds(self, dataToConvert):
		""" converts minutes to seconds """
		return (dataToConvert * 60)

	def convertSecondsToHours(self, dataToConvert):
		""" converts seconds to hours """
		return (dataToConvert / 3600)

	def convertSecondsToMinutes(self, dataToConvert):
		""" converts seconds to minutes """
		return (dataToConvert / 60)

	def convertDaysToHours(self, dataToConvert):
		""" converts days to hours """
		return (dataToConvert * 24)

	def convertDaysToMinutes(self, dataToConvert):
		""" converts days to minutes """
		return (dataToConvert * 1440)

	def convertDaysToSeconds(self, dataToConvert):
		""" converts days to seconds """
		return (dataToConvert * 86400)
	# ---------------------------------------------------
