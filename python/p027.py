import math

ln = 0
la = 0
lb = 0

def is_prime(x):
    if (x < 0):
        return False
    elif (x == 1):
        return False
    elif (x % 2 == 0):
        return False
    else:
        for i in range(3, math.floor(math.sqrt(x)) + 1, 2):
            if (x % i == 0):
                return False
        return True


for a in range(-999,1000):
    for b in range(-999,1001):
        n = 0
        discovered_unprime = False
        while (discovered_unprime == False):
            if (is_prime(n*(n+a) + b)):
                if (n > ln):
                    la = a
                    lb = b
                    ln = n
            else:
                discovered_unprime = True
            n+=1
print (la)
print (lb)
print (la * lb)
