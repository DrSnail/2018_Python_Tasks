class ResultReturnError(Exception):
    def __str__(self):
        return "Result is equal None"

class Operator():
    """
    test
    """
    def __init__(self, operand1: int or float, operand2: int or float):
        self._operand1 = operand1
        self._operand2 = operand2
        self._result = None

    def get_operands(self):
        return self._operand1, self._operand2

    def get_operand(self, operand1 = True):
        if operand1 == True:
            return self._operand1
        elif operand1 == False:
            return self._operand2
        else:
            raise TypeError("Variable \"first\" should to be either True or False")

    def get_result(self, show = False):
        if self._result == None:
            raise ResultReturnError()
        if show == True:
            print(self._result)
        elif show == False:
            return self._result
        else:
            raise TypeError("Variable \"show\" should to be either True or False")


class ADD(Operator):
    def calculate(self):
        self._result = self._operand1 + self._operand2

class SUB(Operator):
    def calculate(self):
        self._result = self._operand1 - self._operand2

class MUL(Operator):
    def calculate(self):
        self._result = self._operand1 * self._operand2

class DIV(Operator):
    def calculate(self):
        self._result = self._operand1 / self._operand2

        if isinstance(self._operand1, int):
            self._result = int(self._result)
        else:
            self._result = float(self._result)


if __name__ == "__main__":
    var1 = 10
    var2 = 2

    custom_input = ADD(var1, var2)
    custom_input.calculate()
    custom_input.get_result(show = True)

    custom_input = SUB(var1, var2)
    custom_input.calculate()
    custom_input.get_result(show=True)

    custom_input = MUL(var1, var2)
    custom_input.calculate()
    custom_input.get_result(show=True)

    custom_input = DIV(var1, var2)
    custom_input.calculate()
    custom_input.get_result(show=True)
