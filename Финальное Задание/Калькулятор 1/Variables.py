class Variable():
    def __init__(self, var_name: str, var_value):
        self.var_name = var_name
        self.var_value = var_value

    def print_value(self):
        print(self.var_value)
