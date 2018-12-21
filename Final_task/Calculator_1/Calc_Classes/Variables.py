from Final_task.Calculator_1.Calc_Classes.ERRORS import *

class Variable():
    def __init__(self, var_name: str, var_value: int or float):
        """
        Класс для любых пользовательских переменных
        :param var_name: Имя переменной
        :type var_name: str
        :param var_value: Значение переменной
        :type var_value: int or float
        """
        # Проверка, можно ли конвертировать имя переменной в int или float, если да, то ошибка
        try:
            var_name = int(var_name)
            var_name = float(var_name)
            raise VariablesTypeError
        except ValueError:
            pass
        self.var_name = var_name
        self.var_value = var_value

    def print_value(self):
        print(self.var_value)
