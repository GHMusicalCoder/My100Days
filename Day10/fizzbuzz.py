def fizzbuzz(n):
    if not n % 3 and not n % 5:
        return 'Fizz Buzz'
    if not n % 3:
        return 'Fizz'
    if not n % 5:
        return 'Buzz'
    return n