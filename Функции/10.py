print("Напишите функцию, которая для заданного в аргументах списка, возвращает как результат перевернутый список")


massive = [1,2,3,4,5,6,7,8,9]


def transpon(massive):
    if isinstance(massive, list) == True:
        for i in range(1, len(massive)+1):
            try:
                temp_massive.append(massive[-i])
            except NameError:
                temp_massive = list()
                temp_massive.append(massive[-i])
        return temp_massive
    else:
        raise Exception("Parameter of transpon function should be list")


print(transpon(massive))