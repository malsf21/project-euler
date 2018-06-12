x = 1
y = 1
counter = 2

while (len(str(y)) < 1000):
    temp = x + y
    x = y
    y = temp
    counter += 1

print(counter)
