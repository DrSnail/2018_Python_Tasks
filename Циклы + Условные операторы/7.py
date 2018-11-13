def fibonachi(a):

    for i in range(2, a+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            try:
                massive.append(i)
            except NameError:
                massive = list()
                massive.append(i)
    return  massive
a = int(input("a="))
massive = fibonachi(a)

pifa = []
for z in range(1, a):
    for y in range(1, z + 1):
        for x in range(1, y + 1):
            if x**2 + y**2 == z**2:
                pifa.append([x, y, z])

print(pifa)