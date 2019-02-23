# File Name: validateandtreatment.py
# Author: Esther Heralta Espinosa
# Date: 02/22/19
# Description of the program: Rock, Paper, Scissors Game

# ---------------------------------- Libraries ----------------------------------
import constant
import screen
# -------------------------------------------------------------------------------

class ValidateTreatment():
	""" This class validates and treats data entered by the user """

	def istValidUserChoice(self, choice):
		""" checks that the option chosen by the user is valid """
		if ((choice == constant.ROCK) | (choice == constant.PAPER) | (choice == constant.SCISSORS) | (choice == constant.EXIT)):
			return (True)
		else:
			return (False)

	def getValidUserChoice(self):
		""" display game menu, prompt the user to enter a valid choice and return it """
		s = screen.Screen()

		s.gameMenu()
		choice = s.getUserChoice()
		while (self.istValidUserChoice(choice) == False):
			s.displayInvalidChoiceMessage()
			s.gameMenu()
			choice = s.getUserChoice()
		return (choice)

	def whoIsTheWinner(self, userOpt, computerOpt):
		""" according to the rules of the game, calculates who is the winner and return it """
		if (((userOpt == constant.ROCK) & (computerOpt == constant.SCISSORS)) | ((userOpt == constant.PAPER) & 
			(computerOpt == constant.ROCK)) | ((userOpt == constant.SCISSORS) & (computerOpt == constant.PAPER))):
			return (constant.USER) #user wins
		elif (((computerOpt == constant.ROCK) & (userOpt ==  constant.SCISSORS)) | ((computerOpt == constant.PAPER) & 
			(userOpt == constant.ROCK)) | ((computerOpt == constant.SCISSORS) & (userOpt == constant.PAPER))):
			return (constant.COMPUTER) #computer wins
		else:
			return(constant.TIE) #tie

	def getStringOpt(self, option):
		""" returns the option chosen as a string """
		if (option == constant.ROCK):
			return ('Rock')
		elif (option == constant.PAPER):
			return ('Paper')
		elif (option == constant.SCISSORS):
			return ('Scissors')

	def getRule(self, userOpt, computerOpt):
		""" get the rule (the reason why the user/computer has won)"""
		# * rock (1) blunts scissors (3) >> RULE1
		# * paper (2) cover rock (1) >> RULE2
		# * scissors (3) cut paper (2) >> RULE3
		if (((userOpt == constant.ROCK) & (computerOpt == constant.SCISSORS)) | ((computerOpt == constant.ROCK) & (userOpt ==  constant.SCISSORS))):
			return (constant.RULE1)
		elif (((userOpt == constant.PAPER) & (computerOpt == constant.ROCK)) | ((computerOpt == constant.PAPER) & (userOpt == constant.ROCK))):
			return (constant.RULE2)
		elif (((userOpt == constant.SCISSORS) & (computerOpt == constant.PAPER)) | ((computerOpt == constant.SCISSORS) & (userOpt == constant.PAPER))):
			return (constant.RULE3)

	def getWinner(self, champion):
		""" get the winner (user or computer) """
		if (champion == constant.USER):
			return (constant.USERWINNER)
		elif (champion == constant.COMPUTER):
			return (constant.COMPUTERWINNER)
