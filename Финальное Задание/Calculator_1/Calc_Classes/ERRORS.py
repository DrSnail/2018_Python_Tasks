class ResultReturnError(Exception):
    def __str__(self):
        return "Result is equal None"

class MultipleVariablesError(Exception):
    def __str__(self):
        return ""