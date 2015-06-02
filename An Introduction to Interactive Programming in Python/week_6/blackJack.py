# Mini-project #6 - Blackjack

import random

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


# load card sprite - 936x384 - source: jfitz.com
CARD_POSITION = ((50, 400), (50, 150))
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

# initialize some useful global variables
in_play = False
dealer_message = ""
player_message = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)


# define hand class
class Hand:
    def __init__(self):
        self.hasAce = False
        self.cards = list()
        self.hand_value = 0

    def __str__(self):
        res = "Hand contains"
        for card in self.cards:
            res += " " + str(card)
        return res

    def add_card(self, card):
        self.cards.append(card)
        self.hand_value += VALUES[card.get_rank()]
        if card.get_rank() == "A":
            self.hasAce = True

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        if not self.hasAce:
            return self.hand_value
        else:
            if self.hand_value + 10 <= 21:
                return self.hand_value + 10
            else:
                return self.hand_value

    def draw(self, canvas, pos):
        offset = 0
        for card in self.cards:
            card.draw(canvas, (pos[0] + offset, pos[1]))
            offset += 100


# define deck class
class Deck:
    def __init__(self):
        self.cards = list()
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

    def __str__(self):
        res = "Deck contains"
        for card in self.cards:
            res += " " + str(card)
        return res


# define event handlers for buttons
def deal():
    global dealer_message, in_play, deck, player, dealer, score, player_message
    if in_play:
        score -= 1

    dealer_message = ""
    deck = Deck()
    deck.shuffle()

    player = Hand()
    dealer = Hand()

    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())

    # print "PLAYER " + str(player) + " value: " + str(player.get_value())
    #print "DEALER " + str(dealer) + " value: " + str(dealer.get_value())

    in_play = True
    player_message = "Hit or stand?"


def hit():
    global player, deck, in_play, score, dealer_message, player_message

    if in_play:
        player.add_card(deck.deal_card())
        # print "PLAYER " + str(player) + " value: " + str(player.get_value())
        if player.get_value() > 21:
            dealer_message = "You have busted"
            in_play = False
            score -= 1
            player_message = "New deal?"
            # if busted, assign a message to outcome, update in_play and score


def stand():
    global in_play, dealer, player, score, dealer_message, player_message

    if not in_play:
        return
    else:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
            # print "DEALER " + str(dealer) + " value: " + str(dealer.get_value())
        if dealer.get_value() > 21:
            dealer_message = "Dealer have busted"
            score += 1
            in_play = False
            player_message = "New deal?"
            return

        if player.get_value() <= dealer.get_value():
            dealer_message = "Dealer wins"
            score -= 1
        else:
            dealer_message = "Player wins"
            score += 1

    in_play = False
    player_message = "New deal?"


# draw handler
def draw(canvas):
    global player, dealer, score

    canvas.draw_text("Blackjack", (180, 40), 50, "Red")
    canvas.draw_text("Scores " + str(score), (450, 315), 25, "Yellow")
    canvas.draw_text("Player", (0, CARD_POSITION[0][1] - 15), 50, "Black")
    canvas.draw_text("Dealer", (0, CARD_POSITION[1][1] - 15), 50, "Black")

    canvas.draw_text(dealer_message, (150, CARD_POSITION[1][1] - 15), 50, "Red")
    canvas.draw_text(player_message, (150, CARD_POSITION[0][1] - 15), 50, "Red")

    player.draw(canvas, CARD_POSITION[0])
    dealer.draw(canvas, CARD_POSITION[1])

    if in_play:
        canvas.draw_image(card_back, (CARD_CENTER[0], CARD_CENTER[1]), CARD_BACK_SIZE,
                          (CARD_POSITION[1][0] + CARD_BACK_CENTER[0], CARD_POSITION[1][1] + CARD_BACK_CENTER[1]), CARD_BACK_SIZE)


deal()
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

# create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit", hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
frame.start()