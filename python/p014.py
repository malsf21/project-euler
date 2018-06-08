lcounter = 0
lchain = 0

def next_step(x):
    if (x % 2 == 0):
        return x/2
    else:
        return (3*x)+1

for i in range(1,1000000):
    counter = 0
    current = i
    while (current != 1):
        current = next_step(current)
        counter += 1
    if (counter > lcounter):
        lcounter = counter
        lchain = i
print(lchain)
