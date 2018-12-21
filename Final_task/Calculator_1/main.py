from Final_task.Calculator_1.Calc_Classes.ERRORS import *
from Final_task.Calculator_1.Calc_Classes.Variables import *
from Final_task.Calculator_1.Calc_Classes.Operators import *
import logging

dynamic_input_dic = {}
dynamic_user_variables_dic = {}
var1 = None
var2 = None
log = logging.getLogger("Errors")

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

        if custom_input[0] == "ADD":
            pass