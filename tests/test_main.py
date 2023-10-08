from calculator.main import Calculator


def test_add_two_numbers():
    calculator = Calculator

    result = calculator.add(7, 4)
    assert result == 11
