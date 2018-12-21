valid_commands = ["ADD", "SUB", "MUL", "DIV", "SET", "PRINT"]

class ResultReturnError(Exception):
    def __str__(self):
        return "Result is equal None"

class MultipleVariablesError(Exception):
    def __str__(self):
        return ""

class InputError(Exception):
    def __str__(self):
        return "Не верная комманда"

class CommandInputError(InputError):
    def __str__(self):
        return "Такой комманды не существует"

class VariableInputError(InputError):
    def __str__(self):
        return "Не вернно введены переменные"