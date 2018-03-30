def longest(words):
    words.sort(key=lambda w: len(w), reverse=True)
    return len(words[0])


print(longest(['explicit', 'is', 'better', 'than', 'implicit']))


# best practice
def longest(words):
    return max(map(len, words))