print("Напишите функцию вычисляющую N-ое число последовательности Фибоначчи")


def fibonachi(n):
    to = 4*10**6
    result = 0
    F1 = 1
    F2 = 1
    fib = [1, 1]
    while result < to:
        result = F1 + F2
        F1 = F2
        F2 = result
        if result < to:
            fib.append(result)
        else:
            pass
    return fib[n]