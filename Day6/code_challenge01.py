# this is for the pybytes code challenge #1
import sys
sys.path.append('/home/chris/PycharmProjects/My100Days/extra_files/')

import my_100days_library as mylib


def load_words():
    """
    loads the dictionary into a list
    :return: the dictionary word list
    """
    return mylib.load_words()


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


words = load_words()
# print(len(words))
# print(words[0])
# print(words[-1])
value, word_list = max_word_value(words)
print('Max Value: {0}, Words: {1}'.format(value, word_list))



