import operator
from functools import reduce


class Calculator:
    def add(*args):
        return sum(args)

    def multiply(*args):
        return reduce(operator.mul, args)
