print("x\ty\tx and y\tx or y\tx and not y\t(x or z) and (y or z)")
for x in range(0,2):
    for y in range(0,2):
        print(str(x) + "\t" + str(y) + "\t" + str(x and y) + "\t" + str(x or y) + "\t" + str(x and not y))