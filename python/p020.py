import math

digits = [int(i) for i in str(math.factorial(100))]
sum = 0
for i in range(len(digits)):
    sum += digits[i]
print(sum)
