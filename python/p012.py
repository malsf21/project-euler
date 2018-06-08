import math

found = False
counter = 0
sum = 0
divisors = 0

while (not found):
    counter += 1
    sum += counter
    divisors = 0
    for i in range(1, math.floor(math.sqrt(sum))+1):
        if (sum % i == 0):
            divisors += 2
        if (i*i == sum):
            divisors -= 1
    if (divisors > 500):
        print(sum)
        found = True
