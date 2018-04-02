from data import DICTIONARY, LETTER_SCORES, POUCH
import random
from  itertools import permutations, chain


def get_letters(count=7):
    """
    grab count # of letters from our pouch
    :param count: the number of letters to return
    :return: a list of count letters
    """
    letters = []
    our_pouch = POUCH
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
    value = 0
    for letter in word:
        if letter != '-':
            value += LETTER_SCORES[letter]
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


def get_possible_words(letters):
    perms = list(permutations(letters, i) for i in range(4, len(letters)+1))
    words = (''.join(p) for p in chain(*perms))
    print(words)
    matches = DICTIONARY.intersection(words)
    print(matches)


def main():
    valid_word = False
    letter_list = get_letters(7)
    while not valid_word:
        user_word = get_user_word(letter_list)
        valid_word = test_word(user_word, letter_list)
    user_word_value = calc_word_value(user_word)
    print('Word chosen: {0} (value: {1})'.format(user_word, user_word_value))
    get_possible_words([x.lower for x in letter_list])


if __name__ == '__main__':
    main()