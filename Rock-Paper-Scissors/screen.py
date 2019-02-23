# File Name: screen.py
# Author: Esther Heralta Espinosa
# Date: 02/22/19
# Description of the program: Rock, Paper, Scissors Game

# ---------------------------------- Libraries ----------------------------------
import constant
import validateandtreatment
# -------------------------------------------------------------------------------

class Screen():
	""" This class contains functions that are related to displaying something on the screen or asking the user to enter some kind of data """
	
	def welcomeMessage(self):
		""" welcome message """
		print("\n")
		print("	************** WELCOME TO THE ROCK, PAPER, SCISSORS GAME **************")
		print("\n")
		print("		Let's play!!")
		print("\n")

	def exitMessage(self):
		""" goodbye message """
		print("\n")
		print("	******************* YOU HAVE EXIT THE GAME. GOODBYE! ******************")
		print("\n")

	def gameMenu(self):
		""" display the game menu """
		print("		1. Rock")
		print("		2. Paper")
		print("		3. Scissors")
		print("		4. Exit")
		print("\n")

	def getUserChoice(self):
		""" prompt the user to enter one of the three possible options """
		userChoice = str(input("	Enter a choice: "))
		return (userChoice)

	def displayInvalidChoiceMessage():
		""" display a message telling the user that the option entered is not valid """
		print("\n")
		print("	Invalid choice. Please, choose a valid one.")

	def displayComputerChoiceMessage(self, computerOpt):
		""" display on the screen the option chose by the computer """
		print("\n")
		vt = validateandtreatment.ValidateTreatment()
		computerChoice = vt.getStringOpt(computerOpt)
		print("	The computer has chosen {0}.".format(computerChoice))

	def displayWinnerMessage(self, winner, userOpt, computerOpt):
		""" display who has won: the computer or the user """
		print("\n")
		vt = validateandtreatment.ValidateTreatment()
		userChoice = vt.getStringOpt(userOpt)
		computerChoice = vt.getStringOpt(computerOpt)
		print("	You chose {0} and the computer chose {1}.".format(userChoice, computerChoice))
		rule = vt.getRule(userOpt, computerOpt)
		print("	* {0}".format(rule))
		print("\n")
		champion = vt.getWinner(winner)
		print("	{0}!".format(champion))
		print("\n")

	def displayTieMessage(self):
		""" display message of tie (no winner) """
		print("\n")
		print("	Tie! There is no winner this time.")
		print("\n")


