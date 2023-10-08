from calculator.main import Calculator


def test_add_two_numbers():
    calculator = Calculator

    result = calculator.add(7, 4)
    assert result == 11


def test_add_many_numbers():
    calculator = Calculator

    result = calculator.add(7, 4, 3)
    assert result == 14


def test_multiply_two_numbers():
    calculator = Calculator

    result = calculator.multiply(2, 4)
    assert result == 8


def test_multiply_many_numbers():
    calculator = Calculator

    result = calculator.multiply(2, 4, 3)
    assert result == 24
