# A small app that creates a number pattern based on the input integer n, built in Python for freeCodeCamp's Number Pattern Generator lap.

def number_pattern(n):
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    if n < 1:
        return 'Argument must be an integer greater than 0.'

    result = ''
    for i in range(1, n+1):
        result += str(i)
        if i < n:
            result += ' '
    
    return result

print(number_pattern(520))