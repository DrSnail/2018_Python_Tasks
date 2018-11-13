# Листинг 2
a = int(input("a="))
for i in range(2, a+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        try:
            massive.append(i)
        except NameError:
            massive = []
            massive.append(i)
print(massive)