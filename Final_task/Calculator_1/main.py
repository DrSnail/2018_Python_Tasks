from .Calc_Classes.Operators import *
from .Calc_Classes.Variables import *

if __name__ == "__main__":
    var1 = Variable("my_name", 10)
    v2 = 2

    custom_input = ADD(var1, v2)
    custom_input.calculate()
    custom_input.get_result(show=True)

    print(var1.var_value)
    pr