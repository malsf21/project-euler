with open("./files/p022_names.txt") as f:
    content = f.readlines()
content = content[0].replace('"', '').split(",")
content = sorted(content)
numsum = 0
for i in range(len(content)):
    numsum += (i+1) * sum([int(ord(x))-64 for x in list(content[i])])
print(numsum)
