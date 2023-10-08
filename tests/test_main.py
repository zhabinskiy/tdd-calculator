from calculator.main import Calculator


def test_add_two_numbers():
    calculator = Calculator

    result = calculator.add(7, 4)
    assert result == 11


def test_add_three_numbers():
    calculator = Calculator

    result = calculator.add(7, 4, 3)
    assert result == 14
