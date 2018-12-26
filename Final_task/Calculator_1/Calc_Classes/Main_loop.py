from Final_task.Calculator_1.Calc_Classes.ERRORS import *
from Final_task.Calculator_1.Calc_Classes.Variables import *
import logging
import re

log = logging.getLogger("Errors")

class Iterator():
    pass

class User_input():
    def __init__(self, user_input: str):
        self._made_operands = None
        self.__print_command = False
        self.__print_or_return_command = None
        self._split_input(user_input)
        self._check_command()

    def _split_input(self, user_input):
        self.user_input = user_input.split()

    def _make_operands(self, dynamic_user_variables_dic):
        """
        Конвертирует пользовательский ввод в int or float or Variable
        :param user_input: строка, которую нужно конвертировать
        :type user_input: int, float, Variable
        :return:
        :rtype:
        """
        for i in range(1, len(self.user_input)):
            if "." in self.user_input[i] or "," in self.user_input[i]:
                try:
                    self.user_input[i] = float(self.user_input[i])
                except ValueError:
                    if self.user_input[i] in dynamic_user_variables_dic:
                        self.user_input[i] = dynamic_user_variables_dic[self.user_input[i]]
                    else:
                        raise VariablesTypeError
            else:
                try:
                    self.user_input[i] = int(self.user_input[i])
                except ValueError:
                    if self.user_input[i] in dynamic_user_variables_dic:
                        self.user_input[i] = dynamic_user_variables_dic[self.user_input[i]]
                    else:
                        raise VariablesTypeError
        self._made_operands = True

    def _check_command(self, user_input:str = None):
        """
        Проверка пользовательской команды на валидность
        :return:
        :rtype:
        """
        if "PRINT" in self.user_input or "RETURN" in self.user_input or "INTO" in self.user_input:
            self.__print_or_return_command = True
            if len(self.user_input) < 2 or len(self.user_input) > 3:
                raise InputError
        else:
            if len(self.user_input) < 3 or len(self.user_input) > 3:
                raise InputError
            elif self.user_input[0] not in valid_commands:
                raise CommandInputError

        if not self.__print_or_return_command:
            if "." in self.user_input[1] or "," in self.user_input[1]:
                self._var1_float = True
            else:
                self._var1_float = False
            if "." in self.user_input[2] or "," in self.user_input[2]:
                self._var2_float = True
            else:
                self._var2_float = False


class Commands(User_input):
    def __init__(self, user_input: str, dynamic_user_variables_dic: dict, skip_make_operands = False):
        super().__init__(user_input)
        self._make_operands(dynamic_user_variables_dic)
        self._dynamic_user_variables_dic = dynamic_user_variables_dic

    def get_operands(self):
        """
        Возвращает операнд (оба)
        :return:
        :rtype:
        """
        return self.user_input[1], self.user_input[2]

    def get_left_operand(self):
        return self.user_input[1]

    def get_right_operand(self):
        return self.user_input[2]

    # def _make_operands(self, dynamic_user_variables_dic):
    #     self._make_operands(dynamic_user_variables_dic)

class SET(Commands):
    def __init__(self, user_input: str, dynamic_user_variables_dic: dict):
        # переопределил метод _make_operands()
        super().__init__(user_input, dynamic_user_variables_dic)

    def _make_operands(self, dynamic_user_variables_dic):
        pass
    def get_right_operand(self) -> None:
        pass
    def get_operands(self) -> None:
        pass

    def set_variable(self, dynamic_user_variables_dic: dict = None):
         if dynamic_user_variables_dic:
             # Проверка, есть ли переменная в списке пользовательских переменных, если нет, то вызов ошибки
             if self.user_input[2] in dynamic_user_variables_dic:
                 self._dynamic_user_variables_dic[self.user_input[1]] = Variable(self.user_input[1], dynamic_user_variables_dic[self.user_input[2]].var_value)
             else:
                 raise VariablesTypeError
         else:
             if self._var2_float:
                 self._dynamic_user_variables_dic[self.user_input[1]] = Variable(self.user_input[1], float(self.user_input[2]))
             else:
                 self._dynamic_user_variables_dic[self.user_input[1]] = Variable(self.user_input[1], int(self.user_input[2]))

class PRINT(Commands):
    def __init__(self, user_input: str, dynamic_user_variables_dic: dict):
        super().__init__(user_input, dynamic_user_variables_dic)

        print(dynamic_user_variables_dic[self.user_input[1].var_name].var_value)

class Functions(Commands):
    def __init__(self, user_input: str, dynamic_user_variables_dic: dict):
        # self.user_input = user_input.split(sep=" ; ")
        super().__init__(user_input, dynamic_user_variables_dic)
        self.__make_user_input(user_input)

    def _make_operands(self, dynamic_user_variables_dic):
        pass
    def _check_command(self, user_input:str = None):
        pass

    def __make_user_input(self, user_input:str):
        self.user_input:list = user_input.split(sep=" : ")
        self.user_input[0]:list = self.user_input[0].split()
        self.user_input[1]:list = self.user_input[1].split()
        self.user_input[-1]:list = self.user_input[-1].split(sep=" ; ")
        for index in range(0, len(self.user_input[-1])):
            self.user_input[-1][index] = self.user_input[-1][index].split()
        # Может так случится, что в конце команды после ; нет никаких пробела. Надо это удалить
        for main_index in range(1, len(self.user_input)):
            for index in range(0, len(self.user_input[main_index])):
                while self.user_input[main_index][index][-1] == " " or self.user_input[main_index][index][-1] == ";":
                    del self.user_input[main_index][index][-1]


class DEF(Functions):
    pass

class CALC(Functions):
    pass

if __name__ == "__main__":
    dynamic_user_variables_dic = {}
    test = Functions('DEF pow2 : x y z a : MUL x x ; ADD x y ; RETURN x ;', dynamic_user_variables_dic)
    print("READY")