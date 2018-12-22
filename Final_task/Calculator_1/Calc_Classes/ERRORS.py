valid_commands = ["ADD", "SUB", "MUL", "DIV", "SET", "PRINT"]

class CalcError(Exception):
    def __str__(self):
        return "Error"

class ResultReturnError(CalcError):
    def __str__(self):
        return "Result is equal None"

class MultipleVariablesError(CalcError):
    def __str__(self):
        return ""

class VariablesTypeError(CalcError):
    def __str__(self):
        return "VariableTypeError. Не вверный тип переменной"

class InputError(CalcError):
    def __str__(self):
        return "Не верная комманда"

class CommandInputError(InputError):
    def __str__(self):
        return "Такой комманды не существует"

class VariableInputError(InputError):
    def __str__(self):
        return "Не вернно введены переменные"