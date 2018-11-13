to = 4*10**6
result = 0
F1 = 1
F2 = 1
while result < to:
    result = F1 + F2
    F1 = F2
    F2 = result
    if result < to:
        print(result)
    else:
        pass
