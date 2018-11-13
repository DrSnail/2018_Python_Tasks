regulator = input("regulator=")
a = int(input("Iterate to="))

massive = []
for i in range(1, a):
    if regulator == "True" or regulator == "true":
        if i % 2 == 0:
            massive.append(i)
    elif regulator == "False" or regulator == "false":
        if i % 2 != 0:
            massive.append(i)
    else:
        raise NameError
print(massive)



