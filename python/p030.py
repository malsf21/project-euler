nums = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                for m in range(10):
                    for n in range(10):
                        if (i**5 + j**5 + k**5 + l**5 + m**5 + n**5 == int(str(i)+str(j)+str(k)+str(l)+str(m)+str(n))):
                            print(int(str(i)+str(j)+str(k)+str(l)+str(m)+str(n)))
                            nums += int(str(i)+str(j)+str(k)+str(l)+str(m)+str(n))
print(nums-1)
