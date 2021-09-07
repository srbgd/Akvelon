"""
Extra module for Fibonacci number computation
"""

from typing import Tuple
from functools import lru_cache

# compute numbers up to 2**BIT_LENGTH without optimization
BIT_LENGTH = 1024


@lru_cache(maxsize=4096)
def karatsuba(x: int, y: int) -> int:
    """
    Karatsuba algorithms for fast multiplication in base 2 with bitwise optimization

    :param x: first multiplier
    :param y: second multiplier
    :return: product
    """

    x_length, y_length = x.bit_length(), y.bit_length()
    if x_length < BIT_LENGTH or y_length < BIT_LENGTH:
        return x * y
    # get the half on the bits of the larger multiplier with bitwise alignment
    half = (max(x_length, y_length) + 32) // 64 * 32
    # get a binary mask with half-1 ones
    mask = (1 << half) - 1
    # compute intermediate values of karatsuba algorithm (z0, z1, z2)
    x_right, y_right = x & mask, y & mask
    x_left, y_left = x >> half, y >> half
    new_x, new_y = x_left + x_right, y_left + y_right
    left = karatsuba(x_left, y_left)
    right = karatsuba(x_right, y_right)
    # next step
    return (((left << half) + karatsuba(new_x, new_y) - left - right) << half) + right


@lru_cache(maxsize=4096)
def inner_fibonacci(n: int) -> Tuple[int, int]:
    """
    Fast doubling fibonacci computation algorithm optimized with Karatsuba multiplication

    :param n: sequential number
    :return: tuple with n'th anh n+1'th fibonacci numbers
    """

    if n == 0:
        return 0, 1
    a, b = inner_fibonacci(n // 2)
    c = karatsuba(a, 2 * b - a)
    d = karatsuba(a, a) + karatsuba(b, b)
    return (c, d) if n % 2 == 0 else (d, c + d)


@lru_cache(maxsize=4096)
def fibonacci(n: int) -> int:
    """
    Compute n'th fibonacci number

    :param n: sequential number
    :return: n'th fibonacci number
    """
    return inner_fibonacci(n)[0]
