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
    value = 0
    for letter in word:
        if letter != '-':
            value += mylib.LETTER_VALUE[letter.upper()]
    return value


def max_word_value(word_list):
    max_value = 0
    max_value_list = []
    for word in word_list:
        value = calc_word_value(word)
        if value > max_value:
            max_value = value
            max_value_list = list()
            max_value_list.append(word)
        elif value == max_value:
            max_value_list.append(word)

    return max_value_list


words = load_words()
# print(len(words))
# print(words[0])
# print(words[-1])
print(max_word_value(words))



