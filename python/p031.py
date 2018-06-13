ways = 1 # bc 2 pound coin
for p100 in range(3):
    for p50 in range(4-2*p100+1):
        for p20 in range(10-5*p100-2*p50+1):
            for p10 in range(20-10*p100-5*p50-2*p20+1):
                for p5 in range(40-20*p100-10*p50-4*p20-2*p10+1):
                    for p2 in range(100-50*p100-25*p50-10*p20-5*p10-2*p5+1):
                        for p1 in range(200-100*p100-50*p50-20*p20-10*p10-5*p5-2*p2+1):
                            if (100*p100 + 50*p50 + 20*p20 + 10*p10 + 5*p5 + 2*p2 + p1 == 200):
                                ways += 1
print(ways)
