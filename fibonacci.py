maxnumber = 10000
preprevious = 0
previous = 1
a = int


def fibonacci(previous, preprevious):
    if previous + preprevious < maxnumber:
        a = preprevious + previous
        print(a)
        previous, preprevious = a, previous
        fibonacci(previous, preprevious)


fibonacci(previous, preprevious)
