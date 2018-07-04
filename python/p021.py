import math

total_sum = 0

def sum_divisors(num):
    divisor_sum = 0
    for i in range(1, int(math.sqrt(num)) + 1):
        if (num/i == math.floor(num/i)):
            divisor_sum += i
            if (i != num/i):
                divisor_sum += num/i
    return divisor_sum - num


for i in range(1,10000):
    if (i == sum_divisors(sum_divisors(i)) and i != sum_divisors(i)):
        total_sum += i

print(total_sum)
