# File Name: main.py
# Author: Esther Heralta Espinosa
# Date: 02/20/19
# Description of the program: Conversion Calculator

"""
The Conversion Calculator converts between commonly used units.
The user can select among different options such as Temperature, Weight, and Time.
Once the user choose among Time, Weight, and Temperature, a submenu is displayed showing the
different kind of conversions that can be carried out.
After a conversion is selected, the user has to enter the value to convert. 
The result of the conversion will be shown on the screen.
"""    

# ---------------------------------- Libraries ----------------------------------
import screen #module
import validate #module
# -------------------------------------------------------------------------------

# -------------------------------- Main Program ---------------------------------

def main():
	s = screen.Screen()
	vd = validate.ValidateData()

	s.mainMenu() #display the main menu on the screen
	opt = s.getMenuOption() #prompt the user to enter an option
	s.getValidMainMenuOption(opt) #validate the option entered

	#depending on the option entered by the user the program will call a specific routine
	while (opt != 4): #while no exit
		if (opt == 1): #temperature
			s.temperatureMenu()
			optTemp = s.getMenuOption()
			s.getValidTemperatureMenuOption(optTemp)
			while (optTemp != 7):
				value = s.getValueToConvert()
				valueConverted = vd.optionTreatmentTemperature(value, optTemp)
				s.displayTemperatureConversionMessage(optTemp, value, valueConverted)
				s.temperatureMenu()
				optTemp = s.getMenuOption()
				s.getValidTemperatureMenuOption(optTemp)
		elif (opt == 2): #weight
			s.weightMenu()
			optWeight = s.getMenuOption()
			s.getValidWeightMenuOption(optWeight)
			while (optWeight != 7):
				value = s.getValueToConvert()
				valueConverted = vd.optionTreatmentWeight(value, optWeight)
				s.displayWeightConversionMessage(optWeight, value, valueConverted)
				s.weightMenu()
				optWeight = s.getMenuOption()
				s.getValidWeightMenuOption(optWeight)
		elif (opt == 3): #time
			s.timeMenu()
			optTime = s.getMenuOption()
			s.getValidTimeMenuOption(optTime)
			while (optTime != 0):
				value = s.getValueToConvert()
				valueConverted = vd.optionTreatmentTime(value, optTime)
				s.displayTimeConversionMessage(optTime, value, valueConverted)
				s.timeMenu()
				optTime = s.getMenuOption()
				s.getValidTimeMenuOption(optTime)

		s.mainMenu() #display the main menu on the screen
		opt = s.getMenuOption() #prompt the user to enter an option
		s.getValidMainMenuOption(opt) #validate the option entered

	s.exitMessage()

if __name__ == "__main__":
	main()
# -------------------------------------------------------------------------------