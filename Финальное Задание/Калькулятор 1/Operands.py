class ResultReturnError(Exception):
    def __str__(self):
        return "Result is equal None"

class Operand():
    def __init__(self, operand1: int, operand2: int):
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

class ADD(Operand):
    def calculate(self):
        self._result = self._operand1 + self._operand2

class SUB(Operand):
    def calculate(self):
        self._result = self._operand1 - self._operand2

class MUL(Operand):
    def calculate(self):
        self._result = self._operand1 * self._operand2

class DIV(Operand):
    def calculate(self):
        self._result = self._operand1 / self._operand2


if __name__ == "__main__":
    custom_input = ADD(2, 4)
    custom_input.calculate()
    custom_input.get_result(show = True)
