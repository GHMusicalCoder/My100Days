# my answer
def replace_exclamation(s):
    vowels = ['A', 'E', "I", 'O', 'U']
    result = ''
    for letter in s:
        if letter.upper() in vowels:
            result += '!'
        else:
            result += letter
    return result


print(replace_exclamation("Hi!"))
print(replace_exclamation("!Hi! Hi!"))
print(replace_exclamation("aeiou"))
print(replace_exclamation("ABCDE"))
print(replace_exclamation("HOWDY"))


# preferred result
def replace_exclamation(s):
    return ''.join('!' if c in 'aeiouAEIOU' else c for c in s)