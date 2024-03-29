__all__ = ("even_odd",)


def even_odd(numbers: list[int]) -> float:
    """Определяет отношение суммы четных элементов списка
    к сумме нечетных.

    Example:
        >> even_odd([1, 2, 3, 4, 5])
        0.6667
    """
    even_numbers = sum(filter(lambda x: x % 2 == 0, numbers))
    odd_numbers = sum(x for x in numbers if x % 2 != 0)
    if not odd_numbers:
        return 0
    return even_numbers / odd_numbers
