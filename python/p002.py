term1 = 1
term2 = 2
sum = 0

while (term1 < 4000000):
    if (term1 % 2 == 0):
        sum += term1
    temp = term1
    term1 = term2
    term2 += temp

print(sum)
