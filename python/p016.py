digits = [int(i) for i in str(2**1000)]
sum = 0
for i in range(len(digits)):
    sum += digits[i]
print(sum)
