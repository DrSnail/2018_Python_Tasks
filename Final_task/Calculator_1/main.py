from Final_task.Calculator_1.Calc_Classes.ERRORS import *
from Final_task.Calculator_1.Calc_Classes.Variables import *
from Final_task.Calculator_1.Calc_Classes.Operators import *
from Final_task.Calculator_1.Calc_Classes.Main_func import *
import logging

dynamic_input_dic = {}
dynamic_user_variables_dic = {}
var1 = None
var1_float = None
var2 = None
var2_float = None
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
        # Разбить строку на команды
        custom_input = custom_input.split()
        # Если пользователь ввел 'q', то завершить исполнение программы
        if custom_input[0] == "q":
            break

        # Проверка пользовательского ввода
        try:
            if len(custom_input) < 3 or len(custom_input) > 3:
                raise InputError
            elif custom_input[0] not in valid_commands:
                raise CommandInputError
        except InputError as err:
            log.warning(err.__str__())
            continue

        # Проверка, является ли переменная значением с точкой, или нет
        if "." in custom_input[1] or "," in custom_input[1]:
            var1_float = True
        else:
            var1_float = False
        if "." in custom_input[2] or "," in custom_input[2]:
            var2_float = True
        else:
            var2_float = False

        # Проверка на команду SET. Если второе значение не цифра вообще, то проверяем, может это значение пользоватльская переменная?
        if custom_input[0] == "SET":
            try:
                if var2_float:
                    dynamic_user_variables_dic[custom_input[1]] = Variable(custom_input[1], float(custom_input[2]))
                else:
                    dynamic_user_variables_dic[custom_input[1]] = Variable(custom_input[1], int(custom_input[2]))
                continue
            except ValueError as err:
                try:
                    # Проверка, есть ли переменная в списке пользовательских переменных, если нет, то вызов ошибки
                    if custom_input[2] in dynamic_user_variables_dic:
                        pass
                    else:
                        raise VariablesTypeError
                    dynamic_user_variables_dic[custom_input[1]] = Variable(custom_input[1], dynamic_user_variables_dic[custom_input[2]].var_value)
                    continue
                except Exception as err:
                    log.warning(err)
                    continue

        # Преобразует строки в соответствующие значения
        try:
            custom_input = make_a_command(custom_input)
        except VariablesTypeError as err:
            log.warning(err.__str__())
            continue

        # Проверка на ввод комманд
        if custom_input[0] == "ADD":
            command = ADD(custom_input[1], custom_input[2])
            command.calculate()
            command.get_result(show=True)


