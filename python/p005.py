import fractions

lcm = 1
for i in range(1,21):
    lcm = i * lcm / (fractions.gcd(i,lcm))

print(int(lcm))
