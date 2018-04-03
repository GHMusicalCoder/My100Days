import random
from itertools import permutations, chain
import sys
sys.path.append('/home/chris/PycharmProjects/My100Days/extra_files/')

import my_100days_library as mylib

DICTIONARY = set(mylib.load_words())


def get_letters(count=7):
    """
    grab count # of letters from our pouch
    :param count: the number of letters to return
    :return: a list of count letters
    """
    letters = []
    our_pouch = mylib.POUCH
    for _ in range(7):
        i = random.randint(0, len(our_pouch) - 1)
        letters.append(our_pouch.pop(i))

    return letters


def get_user_word(letters):
    print('Letters drawn: {0}'.format(', '.join(letters)))
    return input('Form a valid word: ').strip().upper()


def test_word(word, letters):
    for letter in word:
        if letter not in letters:
            print('Your word contained {0} which was not in the list of letters {1}'.format(letter, ', '.join(letters)))
            print('Please try again!')
            return False
    if word.lower() not in DICTIONARY:
        print('Your word could not be found in our dictionary.')
        print('Please try again!')
        return False
    return True


def calc_word_value(word):
    """
    takes the word and calculates it against the imported scrabble letter value chart
    :param word: the word to calculate the value against
    :return: the value
    """
    return mylib.calc_word_value(word)


def max_word_value(word_list):
    """
    take a given list and use the calc_word_value function to determine which word is worth the most
    :param word_list: a list of words
    :return: the word (or list of words if of equal value) that is the highest value of the list
    """
    return mylib.max_word_value(word_list)


def get_possible_words(letters):
    n = len(letters)
    word_list = set()

    while n > 0:
        perms = [''.join(i).lower() for i in permutations(letters, n)]
        matches = DICTIONARY.intersection(perms)
        word_list.update(matches)
        n -= 1

    return word_list


def main():
    valid_word = False
    letter_list = get_letters(7)
    while not valid_word:
        user_word = get_user_word(letter_list)
        valid_word = test_word(user_word, letter_list)
    user_word_value = calc_word_value(user_word)
    print('Word chosen: {0} (value: {1})'.format(user_word, user_word_value))
    max_value, max_list = max_word_value(get_possible_words(letter_list))
    print('Optimal word(s) possible: {0} (value: {1})'.format(max_list, max_value))
    print('You scored: {0:.1f}'.format((user_word_value / max_value) * 100))
    print('-' * 60)
    print('Thank you for playing!')


main()