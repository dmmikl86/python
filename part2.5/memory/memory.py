# implementation of card game - Memory

import random

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

EXPOSED = False
card_indexes = []
numbers = []
exposed_cards = []
cards = {0: True, 1: True, 2: True, 3: True, 4: True, 5: True, 6: True, 7: True, 8: True, 9: True, 10: True, 11: True, 12: True, 13: True, 14: True, 15: True}

# helper function to initialize globals
def new_game():
    global numbers, cards, state, card_indexes
    state = 0
    card_indexes = []
    numbers = range(0, 8)
    numbers.extend(numbers)
    random.shuffle(numbers)
    for card in cards:
        cards[card] = not EXPOSED

# define event handlers
def mouseclick(pos):
    global cards, state, numbers, card_indexes, exposed_cards

    index = pos[0] // 50
    if cards[index] == EXPOSED:
        return

    if state == 0:
        state = 1
    elif state == 1:
        state = 2
    else:
        state = 1
        if numbers[card_indexes[0]] == numbers[card_indexes[1]]:
            exposed_cards.extend(card_indexes)
        else:
            cards[card_indexes[0]] = not EXPOSED
            cards[card_indexes[1]] = not EXPOSED
        card_indexes = []

    card_indexes.append(index)
    cards[index] = EXPOSED

# cards are logically 50x100 pixels in size    
def draw(canvas):
    global numbers
    count = 0
    for number in numbers:
        canvas.draw_text(str(number), (count * 50, 80), 100, 'White')
        x1 = count * 50
        x2 = (count + 1) * 50
        if cards[count]:
            canvas.draw_polygon([(x1, 1), (x1, 99), (x2, 99), (x2, 1)], 1, "Black", "Yellow")
        count += 1

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric