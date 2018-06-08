import math

def is_prime(x):
    if (x % 2 == 0):
        return False
    else:
        for i in range(3, math.floor(math.sqrt(x)) + 1, 2):
            if (x % i == 0):
                return False
        return True

sum = 2

for i in range (3,2000000):
    if (is_prime(i)):
        sum += i
        
print(sum)
