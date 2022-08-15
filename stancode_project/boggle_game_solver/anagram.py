"""
File: anagram.py
Name: Abbie Chen
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    TODO: find out all the possibilities of the string combination in the dictionary
    """
    ####################
    #                  #
    #       TODO:      #
    #                  #
    ####################
    print('----------------------------------')
    print('Welcome to stanCode \" Anagram Generator \" (or -1 to quit)')
    while True:
        s = input('Find anagrams for : ')
        start = time.time()
        if s == EXIT:
            break
        else:
            ans_lst = find_anagrams(s)
            print(f'{len(ans_lst)} anagrams: {ans_lst}')
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary():
    d = []
    with open(FILE, 'r') as f:
        for line in f:
            word = line.split('\n')
            d.append(word[0])
    return d


def find_anagrams(s):
    """
    :param s: string inputted by user
    :return: list contains all different combination of the string that can be found in dictionary
    """
    d = read_dictionary()
    ans = ''
    return find_anagrams_helper(s, len(s), ans, [], [], d)


def find_anagrams_helper(s, s_len, ans, ans_lst, lst, dictionary):
    if len(ans) == s_len:
        if ans in dictionary:
            if ans not in ans_lst:
                ans_lst.append(ans)
                print('Searching...')
                print(f'Found: {ans}')
    else:
        for i in range(len(s)):
            if i in lst:
                pass
            else:
                # choose
                ans += s[i]
                lst.append(i)
                # print(lst)
                # explore
                if has_prefix(ans):
                    find_anagrams_helper(s, s_len, ans, ans_lst, lst, dictionary)
                # un-choose
                ans = ans[:-1]
                lst.pop()

    return ans_lst


def has_prefix(sub_s):
    """
    :param sub_s: uncompleted ans
    :return: bool (whether there is word starting with sub_s)
    """
    d = read_dictionary()
    return has_prefix_helper(sub_s, d)


def has_prefix_helper(sub_s, d):
    for word in d:
        if word.startswith(sub_s):
            return True


if __name__ == '__main__':
    main()
