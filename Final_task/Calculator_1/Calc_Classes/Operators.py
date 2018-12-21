from Final_task.Calculator_1.Calc_Classes.Variables import Variable
from Final_task.Calculator_1.Calc_Classes.ERRORS import *
from typing import Union

class Operator():
    def __init__(self, operand1: Union[int, float, Variable], operand2: Union[int, float, Variable]):
        """
        Базовый класс для всех операторов
        :param operand1: Первая переменная
        :type operand1: int, float, Variable
        :param operand2: Вторая переменная
        :type operand2: int, float, Variable
        """
        if type(operand1) not in [int, float, Variable] or type(operand2) not in [int, float, Variable]:
            raise VariablesTypeError

        # Проверка переменных на класс Variable
        if isinstance(operand1, Variable):
            self._operand1 = operand1.var_value
            self.__operand1_is_Variable = True
            self.__operand1 = operand1
        else:
            self.__operand1_is_Variable = False
            self._operand1 = operand1
        if isinstance(operand2, Variable):
            self._operand2 = operand2.var_value
            self.__operand2_is_Variable = True
        else:
            self.__operand2_is_Variable = False
            self._operand2 = operand2
        self._result = None

    def get_operands(self):
        """
        Возвращает операнд (оба)
        :return:
        :rtype:
        """
        return self._operand1, self._operand2

    def get_operand(self, operand1: bool = True):
        """
        Возвращает операнды (Один)
        :param operand1: Вернуть первый операнд? Если False, то второй
        :type operand1:
        :return:
        :rtype:
        """
        if operand1 == True:
            return self._operand1
        elif operand1 == False:
            return self._operand2
        else:
            raise TypeError("Variable \"first\" should to be either True or False")

    def get_result(self, show: bool = False):
        """
        Вернуть результат операции.
        Если результат ничем не равен, то ошибка ResultReturnError()
        Если первый операнд - переменная, то записывает результат в эту переменную
        :param show: Вывести в консоль результат
        :type show:
        :return:
        :rtype:
        """
        if self._result == None:
            raise ResultReturnError()
        if self.__operand1_is_Variable:
            self.__operand1.var_value = self._result
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
    var_var = Variable("test", 5)
    var1 = 10
    var2 = 2

    custom_input = ADD(var_var, var2)
    custom_input.calculate()
    custom_input.get_result(show = True)
    print(var_var.var_value)

    custom_input = SUB(var1, var2)
    custom_input.calculate()
    custom_input.get_result(show=True)

    custom_input = MUL(var1, var2)
    custom_input.calculate()
    custom_input.get_result(show=True)

    custom_input = DIV(var1, var2)
    custom_input.calculate()
    custom_input.get_result(show=True)
