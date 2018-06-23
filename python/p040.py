decimal_string = ""
counter = 1

while (len(decimal_string) < 1000000):
    decimal_string += str(counter)
    counter += 1

constant = int(decimal_string[0]) * int(decimal_string[9]) * int(decimal_string[99]) * int(decimal_string[999]) * int(decimal_string[9999]) * int(decimal_string[99999]) * int(decimal_string[999999])

print(constant)
