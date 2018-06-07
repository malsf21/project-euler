import math

primes = [2,3]
counter = 4

def is_prime(x):
    if (x % 2 == 0):
        return False
    else:
        for i in range(3, math.floor(math.sqrt(x)) + 1, 2):
            if (x % i == 0):
                return False
        return True

while (len(primes) < 10001):
    if (is_prime(counter)):
        primes.append(counter)
    counter += 1

print(primes[10000])
