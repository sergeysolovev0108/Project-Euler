"""
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(value: int) -> bool:
    str_value = str(value)
    return str_value == str_value[::-1]


def largest_palindrome():
    palindrome_generator = (x * y for x in range(999, 900, -1) for y in range(x, 900, -1) if is_palindrome(x * y))
    return next(palindrome_generator)


print(largest_palindrome())
