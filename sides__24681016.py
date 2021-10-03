sides = [2,4,6,8,10,16]
max = -1
for i in range (len(sides)):
    a = sides[i]
    for j in range (len(sides)):
        b = sides[j]
        for y in range (len(sides)):
            c = sides[y]
            if a+b > c and b+c > a and a+c > b:
                p = 0.5*(a+b+c)
                S = (p*(p-a)*(p-b)*(p-c))**0.5
                if max < S:
                    max = S
print(max)                    