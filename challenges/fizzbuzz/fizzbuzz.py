# Some fancy fizzbuzz implementation!!
def fizzbuzz(n):
    """Write a function which accepts `n` as an argument, and prints the following logic to standard out:
    - If `n` is divisible by `3`, print `fizz`
    - If `n` is divisible by `5`, print `buzz`
    - If `n` is divisible by `3` and `5`, print `fizzbuzz`
    - Else print `n`
    """
    if n % 3 == 0 and n % 5 == 0:
        return 'fizzbuzz'
    if n % 3 == 0:
        return 'fizz'
    if n % 5 == 0:
        return 'buzz'
    else:
        return n
