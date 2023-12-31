import operator
from functools import reduce


class Calculator:
    def add(*args):
        return sum(args)

    def substract(a, b):
        return a - b

    def multiply(*args):
        return reduce(operator.mul, args)

    def divide(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return 0
