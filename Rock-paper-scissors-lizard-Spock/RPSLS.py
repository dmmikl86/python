# Rock-paper-scissors-lizard-Spock template
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
import random

SCISSORS = 'scissors'
LIZARD = 'lizard'
PAPER = 'paper'
SPOCK = 'Spock'
ROCK = 'rock'


def name_to_number(name):
	if name == ROCK:
		return 0
	elif name == SPOCK:
		return 1
	elif name == PAPER:
		return 2
	elif name == LIZARD:
		return 3
	elif name == SCISSORS:
		return 4
	else:
		print "Wrong value : " + name
		return -1


def number_to_name(number):
	if number == 0:
		return ROCK
	elif number == 1:
		return SPOCK
	elif number == 2:
		return PAPER
	elif number == 3:
		return LIZARD
	elif number == 4:
		return SCISSORS
	else:
		print "Wrong value : " + number
		return ''


def rpsls(playerChoiceInName):
	print ''
	computerChoiceInNumber = random.randrange(0, 5)
	computerChoiceName = number_to_name(computerChoiceInNumber)

	print 'Player chooses ' + playerChoiceInName
	print 'Computer chooses ' + computerChoiceName

	if playerChoiceInName == SCISSORS:
		isPlayerWin = computerChoiceName == PAPER or computerChoiceName == LIZARD
	elif playerChoiceInName == PAPER:
		isPlayerWin = computerChoiceName == SPOCK or computerChoiceName == ROCK
	elif playerChoiceInName == ROCK:
		isPlayerWin = computerChoiceName == SCISSORS or computerChoiceName == LIZARD
	elif playerChoiceInName == LIZARD:
		isPlayerWin = computerChoiceName == PAPER or computerChoiceName == SPOCK
	else:  # playerChoiceInName == SPOCK:
		isPlayerWin = computerChoiceName == SCISSORS or computerChoiceName == ROCK

	if (isPlayerWin):
		print 'Player wins!'
	else:
		print 'Computer wins!'


rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")


