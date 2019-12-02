import math

k256 = []
primes = []

i = 2
while len(primes) < 64:
    if i % 2 != 0 :
        primes.append(i)
    i += 1

for i in primes:
    c = i ** (1./3.)
    n = (c - int(c)) * 1000000000
    k256.append(hex(int(n)))

print(k256)