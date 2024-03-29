import math


__all__ = ("is_prime",)


def is_prime(number: int) -> bool:
    """Определяет, является ли число простым.

    Example:
        >> is_prime(0):
        False
        >> is_prime(1):
        False
        >> is_prime(4):
        True
    """
    if number < 2:
        return False
    div = int(number ** 0.5)
    for i in range(2, div + 1):
        if number % i == 0:
            return False
    return True
