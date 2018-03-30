def correct(string):
    fixes = {'0': 'O', '5': 'S', '1': 'I'}
    issue = '015'
    result = ''
    for s in string:
        if s in issue:
            result += fixes[s]
        else:
            result += s
    return result



# best fix
def correct(string):
    return string.translate(str.maketrans("501", "SOI"))