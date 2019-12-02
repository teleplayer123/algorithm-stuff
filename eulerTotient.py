from utils import memo

#function to return greatest common divisor
@memo
def gcd(a,b):
    if a == 0:
        return b
    return gcd(b % a, a)

#method to evaluate eulers totient function
def phi(n):
    result = 1
    for i in range(2, n):
        if(gcd(i, n) == 1):
            result += 1
    return result

 