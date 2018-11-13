a = int(input())

for i in range(1, a+1):
    if a % i == 0:
        try:
            massive.append(i)
        except NameError:
            massive = []
            massive.append(i)

if len(massive) == 2 and a % 1 == 0:
    print("Число %a простое" % a)
else:
    print("%a Is not simple" % a)