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


def rpsls(player_choice_in_name):
	print ''
	computer_choice_in_number = random.randrange(0, 5)
	computer_choice_name = number_to_name(computer_choice_in_number)

	print 'Player chooses ' + player_choice_in_name
	print 'Computer chooses ' + computer_choice_name

	if player_choice_in_name == SCISSORS:
		is_player_win = computer_choice_name == PAPER or computer_choice_name == LIZARD
	elif player_choice_in_name == PAPER:
		is_player_win = computer_choice_name == SPOCK or computer_choice_name == ROCK
	elif player_choice_in_name == ROCK:
		is_player_win = computer_choice_name == SCISSORS or computer_choice_name == LIZARD
	elif player_choice_in_name == LIZARD:
		is_player_win = computer_choice_name == PAPER or computer_choice_name == SPOCK
	else:  # player_choice_in_name == SPOCK:
		is_player_win = computer_choice_name == SCISSORS or computer_choice_name == ROCK

	if is_player_win:
		print 'Player wins!'
	else:
		print 'Computer wins!'


def rpslsNumder(player_choice_in_name):
	computer_choice = random.randrange(0, 5)
	computer_choice_name = number_to_name(computer_choice)
	print
	print 'Player chooses ' + player_choice_in_name
	print 'Computer chooses ' + computer_choice_name
	player_choice = name_to_number(player_choice_in_name)
	result = (player_choice - computer_choice) % 5
	if result == 0:
		print "standoff"
		return
	if result <= 2:
		print "Player Win"
	else:
		print "Computer Win"


rpslsNumder("rock")
rpslsNumder("Spock")
rpslsNumder("paper")
rpslsNumder("lizard")
rpslsNumder("scissors")

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")