lprime = 0
test = 2
number = 600851475143

while (number > 1):
    if (number % test == 0):
        lprime = test
        number = number/test
    else:
        test += 1

print(lprime)
