scrabble_values = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]

LETTER_VALUE = {letter: score for score, letters in scrabble_values
                 for letter in letters.split()}


def load_words():
    """load the words dictionary (DICTIONARY constant) into a list and return it"""
    DICTIONARY = '../extra_files/dictionary.txt'
    wordlist = []
    with open(DICTIONARY) as fin:
        for word in fin.readlines():
            wordlist.append(word.strip())
    return wordlist
