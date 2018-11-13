for i in list(range(0, 1000)):
    if i % 3 == 0 or i % 5 == 0:
        try:
            massive.append(i)
        except NameError:
            massive = list()
            massive.append(i)
print(sum(massive))