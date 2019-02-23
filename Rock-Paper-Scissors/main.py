# File Name: main.py
# Author: Esther Heralta Espinosa
# Date: 02/22/19
# Description of the program: Rock, Paper, Scissors Game

""" 
This projects implements a Rock, Paper, Scissors Game. The user plays against the computer.
- the user chooses among rock, paper, or scissors
- the computer chooses among rock, paper, or scissors
- a message showing the winner of the game is displayed on the screen

Rules:
* rock blunts scissors
* paper cover rock
* scissors cut paper
"""

# ---------------------------------- Libraries ----------------------------------
from random import randint
import constant
import screen
import validateandtreatment
# -------------------------------------------------------------------------------

# -------------------------------- Main Program ---------------------------------
def main():
	s = screen.Screen()
	vt = validateandtreatment.ValidateTreatment()

	s.welcomeMessage()
	userChoice = vt.getValidUserChoice()
	while (userChoice != constant.EXIT):
		computerChoice = str(randint(1,3))
		s.displayComputerChoiceMessage(computerChoice) #display the choice of the computer
		winner = vt.whoIsTheWinner(userChoice, computerChoice) 
		if ((winner == constant.USER) | (winner == constant.COMPUTER)):
			s.displayWinnerMessage(winner, userChoice, computerChoice)
		else:
			s.displayTieMessage()
		userChoice = vt.getValidUserChoice()

	s.exitMessage()

if __name__ == "__main__":
	main()
# -------------------------------------------------------------------------------