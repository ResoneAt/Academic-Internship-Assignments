"""
    Because The assert statement is always True!.Why ? Because it is in Tuple form and always returns true.
    To fix it, we need to remove the assertion from the parentheses so that it can work properly.

    The assert statement is used for programmers testing and debugging,
    and it is not correct to validate data and display it to the user.
    we can disable assert with a simple command. So there is no safe way.
"""


def apply_discount(price: int, discount: float = 0.0) -> int:
    """
    This function obtains the final price by taking the price of a product and its percent discount.
    Using the assert statement, it can raise error if the discount percentage is greater than 100% .
    :param price: price product
    :param discount: discount percent
    :return: Final price with discount
    """
    final_price = int(price*(1-discount))
    assert 0 < final_price <= price, 'message'
    return final_price


def modified_apply_discount(price: int, discount: float = 0.0) -> float | str:
    """
    This function obtains the final price by taking the price of a product and its percent discount.
    Using the if and else statement, it can limit the amount of the discount and display
    an appropriate error message for the user.
    :param price: price product
    :param discount: discount percent
    :return: Final price with discount
    """
    final_price = round(price*(1-discount), 2)
    if 0 < final_price <= price:
        return final_price
    else:
        message = 'The discount percentage you entered is outside the legal limit.' \
                  'The discount must be less than 1'
        return message


