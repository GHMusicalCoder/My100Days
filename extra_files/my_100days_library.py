from collections import namedtuple

Letter = namedtuple('Letter', 'name amount value')

distribution = [Letter(name='A', amount='9', value='1'), Letter(name='B', amount='2', value='3'),
                Letter(name='C', amount='2', value='3'), Letter(name='D', amount='4', value='2'),
                Letter(name='E', amount='12', value='1'), Letter(name='F', amount='2', value='4'),
                Letter(name='G', amount='3', value='2'), Letter(name='H', amount='2', value='4'),
                Letter(name='I', amount='9', value='1'), Letter(name='J', amount='1', value='8'),
                Letter(name='K', amount='1', value='5'), Letter(name='L', amount='4', value='1'),
                Letter(name='M', amount='2', value='3'), Letter(name='N', amount='6', value='1'),
                Letter(name='O', amount='8', value='1'), Letter(name='P', amount='2', value='3'),
                Letter(name='Q', amount='1', value='10'), Letter(name='R', amount='6', value='1'),
                Letter(name='S', amount='4', value='1'), Letter(name='T', amount='6', value='1'),
                Letter(name='U', amount='4', value='1'), Letter(name='V', amount='2', value='4'),
                Letter(name='W', amount='2', value='4'), Letter(name='X', amount='1', value='8'),
                Letter(name='Y', amount='2', value='4'), Letter(name='Z', amount='1', value='10')]

POUCH = list(''.join(list(letter.name * int(letter.amount) for letter in distribution)))

LETTER_VALUE = dict(zip([letter.name for letter in distribution], [int(letter.value) for letter in distribution]))


def load_words():
    """load the words dictionary (DICTIONARY constant) into a list and return it"""
    dictionary = '../extra_files/dictionary.txt'
    with open(dictionary) as f:
        return set([word.strip().lower() for word in f.read().split()])


def calc_word_value(word):
    """
    takes the word and calculates it against the imported scrabble letter value chart
    :param word: the word to calculate the value against
    :return: the value
    """
    value = 0
    for letter in word:
        if letter != '-':
            value += LETTER_VALUE[letter.upper()]
    return value


def max_word_value(word_list):
    """
    take a given list and use the calc_word_value function to determine which word is worth the most
    :param word_list: a list of words
    :return: the word (or list of words if of equal value) that is the highest value of the list
    """
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

    return max_value, max_value_list
