"""
Student code for Word Wrangler game
"""

import urllib2
# import SimpleGUICS2Pygame.codeskulptor as codeskulptor
# import test_wrangler as test
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"

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
    """
    sorted_list = []
    new_list1 = list1[:]
    new_list2 = list2[:]
    while len(new_list1) > 0 or len(new_list2):
        if len(new_list1) == 0:
            sorted_list.extend(new_list2)
            break

        if len(new_list2) == 0:
            sorted_list.extend(new_list1)
            break

        if new_list1[0] <= new_list2[0]:
            sorted_list.append(new_list1.pop(0))
        else:
            sorted_list.append(new_list2.pop(0))

    return sorted_list

def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    unsorted list
    merge_sort should use merge to help sort the list!
    """
    pivot = len(list1) / 2
    if len(list1) == 1 or not list1:
        return list1[:]
    else:
        new_list1 = list1[:pivot]
        new_list2 = list1[pivot:]
        sorted_list = merge(merge_sort(new_list1), merge_sort(new_list2))
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
    if not word:
        return [word]

    first = word[0]
    rest = word[1:]
    rest_strings = gen_all_strings(rest)

    all_strings = list(rest_strings)
    for string in rest_strings:
        for idx in range(len(string)+1):
            new_string = string[:idx] + first + string[idx:]
            all_strings.append(new_string)

    return all_strings

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    a_file = urllib2.urlopen(codeskulptor.file2url(filename))
    return list(a_file.readlines())

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
# print merge_sort([1, 92, 4, 87, 7, 73, 19, 47, 22, 33])
# test.run_remove_duplicates_suite(remove_duplicates)
# test.run_intersect_suite(intersect)
# test.run_merge_sort_suite(merge_sort)
# test.run_merge_suite(merge)
# test.run_gen_all_strings_suite(gen_all_strings)
# print gen_all_strings("123")
