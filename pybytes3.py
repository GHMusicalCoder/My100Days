import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)
scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}


# start coding

def load_words():
    """load the words dictionary (DICTIONARY constant) into a list and return it"""
    wordlist = []
    with open(DICTIONARY) as fin:
        for word in fin.readlines():
            wordlist.append(word.strip())
    return wordlist


def calc_word_value(word):
    """given a word calculate its value using LETTER_SCORES"""
    score = 0
    for letter in word:
        score += LETTER_SCORES[letter.upper()]
    return score



def max_word_value(words=None):
    """given a list of words return the word with the maximum word value"""
    if words is not None:
        max_value_word = ''
        max_value = 0
        for word in words:
            if calc_word_value(word) > max_value:
                max_value = calc_word_value(word)
                max_value_word = word

        return max_value_word


valid_words = load_words()
print(len(valid_words))
print(LETTER_SCORES)
print(calc_word_value('bob'))
print(max_word_value(valid_words[20000:21000]))