from .Variables import Variable
from .ERRORS import *

class Operator():
    def __init__(self, operand1: int or float or Variable, operand2: int or float or Variable):
        if isinstance(operand1, Variable):
            self._operand1 = operand1.var_value
            self.__operand1_is_Variable = True
        else:
            self._operand1 = operand1
        if isinstance(operand2, Variable):
            self._operand2 = operand2.var_value
            self.__operand2_is_Variable = True
        else:
            self._operand2 = operand2
        self._result = None

    def get_operands(self):
        return self._operand1, self._operand2

    def get_operand(self, operand1: bool = True):
        if operand1 == True:
            return self._operand1
        elif operand1 == False:
            return self._operand2
        else:
            raise TypeError("Variable \"first\" should to be either True or False")

    def get_result(self, show: bool = False):
        if self._result == None:
            raise ResultReturnError()
        if show == True:
            print(self._result)
        else:
            return self._result

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
