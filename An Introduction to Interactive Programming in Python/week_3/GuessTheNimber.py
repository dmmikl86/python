# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import math

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


secret_number = 0
new_range = 100
n = 0
# helper function to start and restart the game


def new_game():
    global secret_number, n
    secret_number = random.randint(0, new_range)
    n = int(math.ceil(math.log(new_range + 1, 2)))
    print
    print 'New game. Range is from 0 to ', new_range
    print 'Number of remaining guesses is ', n


def range100():
    global new_range
    new_range = 100
    new_game()


def range1000():
    global new_range
    new_range = 1000
    new_game()


def input_guess(guess):
    global n
    input_number = int(guess)
    print
    print "Guess was ", input_number

    n -= 1

    if input_number == secret_number:
        print 'Correct'
        new_game()
        return
    elif input_number > secret_number:
        print 'Number of remaining guesses is ', n
        print 'Higher'
    elif input_number < secret_number:
        print 'Number of remaining guesses is ', n
        print 'Lower'

    if n == 0:
        print 'You ran out of guesses.  The number was', secret_number
        new_game()
        return

# create frame
frame = simplegui.create_frame('GuessTheNumber', 200, 200)

# register event handlers for control elements and start frame
frame.add_button('Range [0-100]', range100, 150)
frame.add_button('Range [0-1000]', range1000, 150)
frame.add_input('Enter Number', input_guess, 150)

# call new_game 
new_game()

frame.start()
