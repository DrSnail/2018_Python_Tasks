from Final_task.Calculator_1.Calc_Classes.ERRORS import *
from Final_task.Calculator_1.Calc_Classes.Variables import *
from Final_task.Calculator_1.Calc_Classes.Operators import *
from Final_task.Calculator_1.Calc_Classes.Main_func import *
import logging

dynamic_input_dic = {}
dynamic_user_variables_dic = {}
var1 = None
var2 = None
log = logging.getLogger("Errors")

def make_a_command(custom_input):
    try:
        custom_input = int(custom_input)
    except ValueError:
        pass
    return custom_input

if __name__ == "__main__":
    while True:
        custom_input = input("$:")
        # Разбить строку на команды
        custom_input = custom_input.split()
        # Если пользователь ввел 'q', то завершить исполнение программы
        if custom_input[0] == "q":
            break

        try:
            if len(custom_input) < 3 or len(custom_input) > 3:
                raise InputError
            elif custom_input[0] not in valid_commands:
                raise CommandInputError
        except InputError as err:
            log.warning(err.__str__())
            continue
        for i in range(1, len(custom_input)):
            custom_input[i] = make_a_command(custom_input[i])

        if custom_input[0] == "SET":
            try:
                dynamic_user_variables_dic[custom_input[1]] = Variable(custom_input[1], int(custom_input[2]))
            except Exception as err:
                log.warning(err)
        if custom_input[0] == "ADD":
            command = ADD(custom_input[1], custom_input[2])
            command.calculate()
            command.get_result(show=True)


