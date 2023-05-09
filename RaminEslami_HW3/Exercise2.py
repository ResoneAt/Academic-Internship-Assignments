import math


def start_zero_p(a: str, b: str) -> str | None:
    """ Raise the error For numbers that start with zero """
    if (len(a) > 1 and a[0] == '0' and a[1] != '.') or (len(b) > 1 and b[0] == '0' and b[1] != '.'):
        error = 'leading zeros in decimal integer literals are not permitted,' \
               'Please fix it ( enter a correct number! ) and try again'
        return error
    return None


def start_zero_n(a: str, b: str) -> str | None:
    """ Raise the error For negative numbers that start with zero """
    if (len(a) > 2 and a[0:2] == '-0' and a[2] != '.') or (len(b) > 2 and b[0:2] == '-0' and b[2] != '.'):
        error = 'leading zeros in decimal integer literals are not permitted,' \
               'Please fix it ( enter a correct number! ) and try again'
        return error
    return None


def check_leading_zero(a: str, b: str) -> str | None:
    """Check the numbers that start with zero"""
    zero_error_n = start_zero_n(a, b)
    zero_error_p = start_zero_p(a, b)
    if zero_error_n is not None:
        return zero_error_n
    if zero_error_p is not None:
        return zero_error_p


def div(a: str, b: str) -> float | str:
    """
    This function divides two numbers and covers all different error cases
    :param a: The numerator
    :param b: Denominator
    :return: The result of division
    """
    leading_zero_error = check_leading_zero(a, b)
    if leading_zero_error is not None:
        return leading_zero_error

    try:
        a, b = float(a), float(b)
        return a / b

    except ZeroDivisionError:
        return math.inf
        # or we can : return complex(float('inf'), float('inf'))

    except ValueError:
        return 'check your input,You have ValueError. Please fix it ( enter a correct number! ) and try again'


def main():
    num1, num2 = input('Enter num1: '), input('Enter num2: ')
    print(div(num1, num2))


if __name__ == "__main__":
    main()
