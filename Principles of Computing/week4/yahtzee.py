"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import SimpleGUICS2Pygame.codeskulptor as codeskulptor
#import codeskulptor

codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """

    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set

def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    max_value = []
    item_count = [hand.count(item) for item in hand]
    for idx in range(len(hand)):
        max_value.append(hand[idx] * item_count[idx])
    # print "hand to evaluate: " + str(hand) + " hand value:" + str(max(max_value))
    return max(max_value)

def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    value = 0.0
    sequences = gen_all_sequences(range(1, num_die_sides + 1), num_free_dice)
    for seq in sequences:
        value += score(held_dice + seq)
    return float(value / len(sequences))

def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    new_hand = [()]
    for item in hand:
        for subset in new_hand:
            new_hand = new_hand + [tuple(subset) + (item, )]

    return set(new_hand)

def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    result = (0.0, ())
    current_value = 0.0

    for item in gen_all_holds(hand):
        value = expected_value(item, num_die_sides, len(hand) - len(item))
        if value > current_value:
            current_value = value
            result = (current_value, item)

    return result

def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (6,6,2,4,4)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score

run_example()

#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
                                       
    
    
    



