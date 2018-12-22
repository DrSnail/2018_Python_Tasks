from Final_task.Calculator_1.Calc_Classes.ERRORS import *
from Final_task.Calculator_1.Calc_Classes.Variables import *
from Final_task.Calculator_1.Calc_Classes.Operators import *
from Final_task.Calculator_1.Calc_Classes.Main_loop import *
import logging

dynamic_input_dic = {}
dynamic_user_variables_dic = {}
log = logging.getLogger("Errors")

def make_a_command(custom_input):
    """
    Конвертирует пользовательский ввод в int
    :param custom_input: строка, которую нужно конвертировать
    :type custom_input: int, float, Variable
    :return:
    :rtype:
    """
    for i in range(1, len(custom_input)):
        if "." in custom_input[i] or "," in custom_input[i]:
            try:
                custom_input[i] = float(custom_input[i])
            except ValueError:
                if custom_input[i] in dynamic_user_variables_dic:
                    custom_input[i] = dynamic_user_variables_dic[custom_input[i]]
                else:
                    raise VariablesTypeError
        else:
            try:
                custom_input[i] = int(custom_input[i])
            except ValueError:
                if custom_input[i] in dynamic_user_variables_dic:
                    custom_input[i] = dynamic_user_variables_dic[custom_input[i]]
                else:
                    raise VariablesTypeError
    return custom_input

if __name__ == "__main__":
    while True:
        custom_input = input("$:")

        # Если ввели 'q', то завершается работа программы
        if custom_input == "q":
            break

        # Обработка комманды PRINT
        elif "PRINT" in custom_input:
            try:
                PRINT(custom_input, dynamic_user_variables_dic)
            except CalcError as err:
                log.warning(err.__str__())
                continue

        # Проверка на команду SET.
        elif "SET" in custom_input:
            try:
                SET(custom_input, dynamic_user_variables_dic).set_variable()
            except ValueError as err:
                try:
                    SET(custom_input, dynamic_user_variables_dic).set_variable(dynamic_user_variables_dic)
                    continue
                except CalcError as err:
                    log.warning(err.__str__())
                    continue

        # Проверка на ввод Математических комманд
        elif "ADD" in custom_input:
            try:
                command = ADD(custom_input, dynamic_user_variables_dic)
            except CalcError as err:
                log.warning(err.__str__())
                continue
            command.calculate()
            command.get_result(show=True)
        elif "SUB" in custom_input:
            try:
                command = SUB(custom_input, dynamic_user_variables_dic)
            except CalcError as err:
                log.warning(err.__str__())
                continue
            command.calculate()
            command.get_result(show=True)
        elif "MUL" in custom_input:
            try:
                command = MUL(custom_input, dynamic_user_variables_dic)
            except CalcError as err:
                log.warning(err.__str__())
                continue
            command.calculate()
            command.get_result(show=True)
        elif "DIV" in custom_input:
            try:
                command = DIV(custom_input, dynamic_user_variables_dic)
            except CalcError as err:
                log.warning(err.__str__())
                continue
            command.calculate()
            command.get_result(show=True)
        else:
            log.warning("Не верно введена комманда")
