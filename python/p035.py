import math

num = 1

def is_prime(x):
    if (x == 1):
        return False
    elif (x % 2 == 0):
        return False
    else:
        for i in range(3, math.floor(math.sqrt(x)) + 1, 2):
            if (x % i == 0):
                return False
        return True

for i in range(3,1000000):
    circular_prime = True
    for j in range(len(str(i))):
        if (not is_prime(int(str(i)[j:] + str(i)[:j]))):
            circular_prime = False
            break
    if (circular_prime == True):
        num += 1

print(num)
