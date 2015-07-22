"""
Test suite for list manipulation functions  in "Word Wrangle"
"""

import poc_simpletest


def run_remove_duplicates_suite(remove_duplicates_function):
    """
    Some informal testing code for remove_duplicates_function
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # test remove_duplicates_function on various inputs
    suite.run_test(remove_duplicates_function([]), [], "remove dups []")
    suite.run_test(remove_duplicates_function([1]), [1], "remove dups [1]")
    suite.run_test(remove_duplicates_function([1, 2]), [1, 2], "remove dups [1, 2]")
    suite.run_test(remove_duplicates_function([1, 1]), [1], "remove dups [1, 1]")
    suite.run_test(remove_duplicates_function([1, 1, 2]), [1, 2], "remove dups [1, 1, 2]")
    suite.run_test(remove_duplicates_function([1, 2, 2]), [1, 2], "remove dups [1, 2, 2]")
    suite.run_test(remove_duplicates_function([1, 1, 2, 2]), [1, 2], "remove dups [1, 1, 2, 2]")
    suite.run_test(remove_duplicates_function([1, 1, 1, 2, 2, 2]), [1, 2], "remove dups [1, 1, 1, 2, 2, 2]")
    
    suite.run_test(remove_duplicates_function(['a']), ['a'], "remove dups [1]")
    suite.run_test(remove_duplicates_function(['a', 'b']), ['a', 'b'], "remove dups [1, 2]")
    suite.run_test(remove_duplicates_function(['a', 'a']), ['a'], "remove dups [1, 1]")
    suite.run_test(remove_duplicates_function(['a', 'a', 'b']), ['a', 'b'], "remove dups [1, 1, 2]")
    suite.run_test(remove_duplicates_function(['a', 'b', 'b']), ['a', 'b'], "remove dups [1, 2, 2]")
    suite.run_test(remove_duplicates_function(['a', 'a', 'b', 'b']), ['a', 'b'], "remove dups [1, 1, 2, 2]")
    suite.run_test(remove_duplicates_function(['a', 'a', 'a', 'b', 'b', 'b']), ['a', 'b'], "remove dups [1, 1, 1, 2, 2, 2]")

    suite.run_test(remove_duplicates_function("aa"), ['a'], "remove dups aa")
    suite.run_test(remove_duplicates_function("aabbbc"), ['a', 'b', 'c'], "remove dups aabbbc")


    
    suite.report_results()
    
    
def run_intersect_suite(intersect_function):
    """
    Some informal testing code for intersect_function
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # test intersect_function on various inputs
    suite.run_test(intersect_function([], []), [], "intersect test 1")
    suite.run_test(intersect_function([], [1]), [], "intersect test 3")
    suite.run_test(intersect_function([1], []), [], "intersect test 4")
    suite.run_test(intersect_function([1], [1]), [1], "intersect test 5")
    suite.run_test(intersect_function([], [1 , 2]), [], "intersect test 6")
    suite.run_test(intersect_function([1 , 2], []), [], "intersect test 7")
    suite.run_test(intersect_function([1], [1 , 2]), [1], "intersect test 8")
    suite.run_test(intersect_function([1, 2], [1]), [1], "intersect test 9")
    suite.run_test(intersect_function([1, 2], [1 , 2]), [1, 2], "intersect test 10")
    suite.run_test(intersect_function([1, 1, 2], [1 , 2]), [1, 2], "intersect test 10A")
    suite.run_test(intersect_function([1, 2], [1 , 1, 2]), [1, 2], "intersect test 10B")
    suite.run_test(intersect_function([1, 2, 2], [1 , 2]), [1, 2], "intersect test 10C")
    suite.run_test(intersect_function([1, 2], [1 , 2, 2]), [1, 2], "intersect test 10D")
    suite.run_test(intersect_function([1, 1, 2], [1 , 2, 2]), [1, 2], "intersect test 11")
    suite.run_test(intersect_function([1, 1, 2], [1 , 1, 2]), [1, 2], "intersect test 11A")
    suite.run_test(intersect_function([1, 2, 2], [1 , 2, 2]), [1, 2], "intersect test 11B")
    
    suite.run_test(intersect_function([1, 2], [2, 3]), [2], "intersect test 12")
    suite.run_test(intersect_function([2, 3], [1, 2]), [2], "intersect test 13")
    suite.run_test(intersect_function([8, 19, 32, 47], [1, 5, 7, 8]), [8], "intersect test 14")
      
    suite.run_test(intersect_function(['a', 'b', 'c'], ['a', 'b']), ['a', 'b'], "intersect test 20")
    
    suite.report_results()
    
    
def run_merge_suite(merge_function):
    """
    Some informal testing code for merge_function
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # test merge_function on various inputs
    suite.run_test(merge_function([], []), [], "merge test 1")
    suite.run_test(merge_function([], [1]), [1], "merge test 3")
    suite.run_test(merge_function([1], []), [1], "merge test 4")
    suite.run_test(merge_function([1], [1]), [1, 1], "merge test 5")
    suite.run_test(merge_function([], [1 , 2]), [1, 2], "merge test 6")
    suite.run_test(merge_function([1 , 2], []), [1, 2], "merge test 7")
    suite.run_test(merge_function([1, 3], [2, 4]), [1, 2, 3, 4], "merge test 8")
    suite.run_test(merge_function([2, 4], [1, 3]), [1, 2, 3, 4], "merge test 9")
    suite.run_test(merge_function([1], [1 , 2]), [1, 1, 2], "merge test 10")
    suite.run_test(merge_function([1, 2], [1]), [1, 1, 2], "merge test 11")
    suite.run_test(merge_function([1, 2], [1 , 2]), [1, 1, 2, 2], "merge test 12")
    suite.run_test(merge_function([1, 1, 2], [1 , 2, 2]), [1, 1, 1, 2, 2, 2], "merge test 13")

    
    suite.run_test(merge_function(['a', 'b', 'c'], ['a', 'b']), ['a', 'a', 'b', 'b', 'c'], "merge test 12")
    
    suite.report_results()    
      

def run_merge_sort_suite(merge_sort_function):
    """
    Some informal testing code for merge_sort_function
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # test merge_sort_function on various inputs
    suite.run_test(merge_sort_function([]), [], "merge_sort []")
    suite.run_test(merge_sort_function([1]), [1], "merge_sort [1]")
    suite.run_test(merge_sort_function([1, 1]), [1, 1], "merge_sort [1, 1]")
    suite.run_test(merge_sort_function([1, 2]), [1, 2], "merge_sort [1, 2]")
    suite.run_test(merge_sort_function([2, 1]), [1, 2], "merge_sort [2, 1]")
    suite.run_test(merge_sort_function([1, 2, 3]), [1, 2, 3], "merge_sort [1, 2, 3]")
    suite.run_test(merge_sort_function([1, 3, 2]), [1, 2, 3], "merge_sort [1, 3, 2]")
    suite.run_test(merge_sort_function([2, 1, 3]), [1, 2, 3], "merge_sort [2, 1, 3]")
    suite.run_test(merge_sort_function([2, 3, 1]), [1, 2, 3], "merge_sort [2, 3, 1]")
    suite.run_test(merge_sort_function([3, 1, 2]), [1, 2, 3], "merge_sort [3, 1, 2]")
    suite.run_test(merge_sort_function([3, 2, 1]), [1, 2, 3], "merge_sort [3, 2, 1]")
    suite.run_test(merge_sort_function([4, 3, 2, 1]), [1, 2, 3, 4], "merge_sort [4, 3, 2, 1]")
    
    
    suite.run_test(merge_sort_function(['a']), ['a'], "merge_sort a")
    suite.run_test(merge_sort_function(['a', 'b']), ['a', 'b'], "merge_sort a b")
    suite.run_test(merge_sort_function(['b', 'a']), ['a', 'b'], "merge_sort b a")
   
    suite.report_results()


def run_gen_all_strings_suite(gen_all_strings_function):
    """
    Some informal testing code for gen_all_strings_function
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # test gen_all_strings_function on various inputs
    suite.run_test(gen_all_strings_function(""),  [""], "gen_all_strings ''")
    suite.run_test(gen_all_strings_function("a"),  ["", "a"], "gen_all_strings 'a'")
    suite.run_test(gen_all_strings_function("ab"),  ["", "b", "a", "ab", "ba"], "gen_all_strings 'ab'")
    suite.run_test(gen_all_strings_function("aab"),  ["", "b", "a", "ab", "ba", "a", "ab", "ba", "aa", "aa", "aab", "aab", "aba", "aba", "baa", "baa"], "gen_all_strings 'aab'")


    suite.report_results()    
