from functools import wraps
from itertools import takewhile
import math
import decimal

def memo(func):
    cache = {}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

@memo
def fib_rec(n):
    if n < 2:
        return 1
    return fib_rec(n - 1) + fib_rec(n - 2)

@memo
def fib(n):
    x, y = 1, 1
    while n > 2:
        x, y = y, x + y
        n -= 1
        if y % 2 == 0:
            yield y

def path_count(n, k):
    if k == 0:
        return 1
    if n == 0:
        return 0
    return path_count(n-1, k-1) + path_count(n-1, k)

def fib_list(n):
    lst = [0, 1]
    for i in range(2, n+1):
            lst.append((lst[i-1]) + (lst[i-2]))
    return lst

def count_evens(seq):
    c = 0
    for i in seq:
        if i % 2 == 0 and i != 0:
            c += 1
    return c

def sum_evens(seq):
    s = 0
    lst = []
    for i in seq:
        if i % 2 == 0:
            lst.append(i)
    s = sum([i for i in lst])
    res = "{0:.2e}".format(decimal.Decimal(s))
    return res

def evens_list(seq):
    lst = []
    for i in seq:
        if i % 2 == 0 and i != 0:
            lst.append(i)
    return lst

#f = fib(4000000)
#print(sum(takewhile(lambda x: x < 4000000, f)))
print(fib_rec(100))