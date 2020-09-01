"""
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def ssk():
    ks = 0  # The sum of the squares
    sk = 0  # The square of the sum
    for x in range(1, 101, 1):
        ks += x
        sk += x**2
    res = ks**2 - sk
    return res


print(ssk())
