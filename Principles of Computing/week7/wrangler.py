"""
Student code for Word Wrangler game
"""

import urllib2
import SimpleGUICS2Pygame.codeskulptor as codeskulptor
import test_wrangler as test
# import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"

# Helper functions
def rec_sorted(list, from_index, to_index):
    """
    sorting list in recursive way
    """
    pivot_index = (to_index - from_index) / 2
    pivot_value = list[pivot_index]
    # todo: sort list
    return list


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    unique_list = []
    for item in list1:
        if not item in unique_list:
            unique_list.append(item)
    return unique_list

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """

    intersect_list = []
    for item in list1:
        if item in list2:
            intersect_list.append(item)
    return remove_duplicates(intersect_list)

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """
    return []

def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    from_index = 0
    to_index = len(list1) - 1
    sorted_list = rec_sorted(list1[:], from_index, to_index)
    return sorted_list

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    return []

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    return []

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates,
                                     intersect, merge_sort,
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
# run()

# Test
test.run_remove_duplicates_suite(remove_duplicates)
test.run_intersect_suite(intersect)
test.run_merge_sort_suite(merge_sort)
test.run_merge_suite(merge)
test.run_gen_all_strings_suite(gen_all_strings)
