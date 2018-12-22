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
        inpt = User_input(input("$:"))

        # Если ввели 'q', то завершается работа программы
        if custom_input == "q":
            break

        # Обработка комманды PRINT
        elif inpt.user_input[0] == "PRINT":
            try:
                PRINT(custom_input, dynamic_user_variables_dic)
            except VariablesTypeError as err:
                log.warning(err.__str__())
                continue

        # Проверка на команду SET. Если второе значение не цифра вообще, то проверяем, может это значение пользоватльская переменная?
        if inpt.user_input[0] == "SET":
            try:
                if var2_float:
                    dynamic_user_variables_dic[inpt.user_input[1]] = Variable(inpt.user_input[1], float(inpt.user_input[2]))
                else:
                    dynamic_user_variables_dic[inpt.user_input[1]] = Variable(inpt.user_input[1], int(inpt.user_input[2]))
                continue
            except ValueError as err:
                try:
                    # Проверка, есть ли переменная в списке пользовательских переменных, если нет, то вызов ошибки
                    if inpt.user_input[2] in dynamic_user_variables_dic:
                        pass
                    else:
                        raise VariablesTypeError
                    dynamic_user_variables_dic[inpt.user_input[1]] = Variable(inpt.user_input[1], dynamic_user_variables_dic[inpt.user_input[2]].var_value)
                    continue
                except Exception as err:
                    log.warning(err)
                    continue

        # Преобразует строки в соответствующие значения
        try:
            inpt.make_operands()
        except VariablesTypeError as err:
            log.warning(err.__str__())
            continue

        # Проверка на ввод Математических комманд
        if inpt.user_input[0] == "ADD":
            command = ADD(inpt.user_input[1], inpt.user_input[2])
            command.calculate()
            command.get_result(show=True)
        elif user_input[0] == "SUB":
            command = SUB(inpt.user_input[1], inpt.user_input[2])
            command.calculate()
            command.get_result(show=True)
        elif user_input[0] == "MUL":
            command = MUL(inpt.user_input[1], inpt.user_input[2])
            command.calculate()
            command.get_result(show=True)
        elif user_input[0] == "DIV":
            command = DIV(inpt.user_input[1], inpt.user_input[2])
            command.calculate()
            command.get_result(show=True)



