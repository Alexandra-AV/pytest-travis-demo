def fizzbuzz(n):
    if not isinstance(n, int):
        raise TypeError('requires int')
    if n <= 0:
        raise TypeError('requires positive int')
    if n % (3*5) == 0: #nebo rovnou 15
        return 'fizzbuzz'
    elif n % 3 == 0:
        return'fizz'
    elif n % 5 == 0:
        return 'buzz'

    return str(n)
