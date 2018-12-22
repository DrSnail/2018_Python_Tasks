from Final_task.Calculator_1.Calc_Classes.ERRORS import *

class Iterator():
    pass

class User_input():
    def __init__(self, user_input: str):
        self.user_input = user_input.split()
        self.__containt_PRINT_command = None
        self.__user_input_contain_print()

    def make_operands(self, dynamic_user_variables_dic):
        """
        Конвертирует пользовательский ввод в int
        :param custom_input: строка, которую нужно конвертировать
        :type custom_input: int, float, Variable
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

    def __user_input_contain_print(self):
        for i in self.user_input:
            if "." in self.user_input[0] or "," in self.user_input[0]:
                self.__containt_PRINT_command = True
            else:
                self.__containt_PRINT_command = False

    def try_command(self):
        if "PRINT" in self.user_input:
            if len(self.user_input) < 2 or len(self.user_input) > 3:
                raise InputError
        else:
            if len(self.user_input) < 3 or len(self.user_input) > 3:
                raise InputError
            elif self.user_input not in valid_commands:
                raise CommandInputError
        # try:
        #     if "PRINT" in self.user_input and (len(self.user_input) < 2 or len(self.user_input) > 2):
        #         raise InputError
        #     elif (len(self.user_input) < 3 or len(self.user_input) > 3) and not "PRINT" in self.user_input:
        #         raise InputError
        #     elif self.user_input[0] not in valid_commands:
        #         raise CommandInputError
        # except InputError as err:
        #     log.warning(err.__str__())
