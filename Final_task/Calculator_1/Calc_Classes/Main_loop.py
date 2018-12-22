from Final_task.Calculator_1.Calc_Classes.ERRORS import *
from Final_task.Calculator_1.Calc_Classes.Variables import *
import logging

log = logging.getLogger("Errors")

class Iterator():
    pass

class User_input():
    def __init__(self, user_input: str):
        self.user_input = user_input.split()
        self._made_operands = None
        self.__print_command = False
        self.__check_command()

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

    def __check_command(self):
        """
        Проверка пользовательской команды на валидность
        :return:
        :rtype:
        """
        if "PRINT" in self.user_input:
            self.__print_command = True
            if len(self.user_input) < 2 or len(self.user_input) > 3:
                raise InputError
        else:
            if len(self.user_input) < 3 or len(self.user_input) > 3:
                raise InputError
            elif self.user_input[0] not in valid_commands:
                raise CommandInputError

        if not self.__print_command:
            if "." in self.user_input[1] or "," in self.user_input[1]:
                self._var1_float = True
            else:
                self._var1_float = False
            if "." in self.user_input[2] or "," in self.user_input[2]:
                self._var2_float = True
            else:
                self._var2_float = False


class Commands(User_input):
    def __init__(self, user_input: str, dynamic_user_variables_dic: dict, user_command_is_set = False):
        super().__init__(user_input)
        if not user_command_is_set:
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

class SET(Commands):
    def __init__(self, user_input: str, dynamic_user_variables_dic: dict):
        super().__init__(user_input, dynamic_user_variables_dic, True)

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
