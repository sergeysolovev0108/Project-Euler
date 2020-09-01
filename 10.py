"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import math


def is_prime(num):
    """Checks if num is prime number"""
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


n = 1
s = []

while True:
    if is_prime(n) is True:
        s.append(n)
    if n == 2000000:
        break
    n += 1


print(sum(s))
