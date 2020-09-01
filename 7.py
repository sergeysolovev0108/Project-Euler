"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import math
from datetime import datetime
start_time = datetime.now()


def is_prime(num):
    """Checks if num is prime number"""
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


prime = [2, 3]
print(len(prime))

i = 5
while True:
    if is_prime(i) is True:
        prime.append(i)
    if len(prime) == 10001:
        break
    i += 1


print(prime[-1])

print('ВРЕМЯ ВЫПОЛНЕНИЯ', datetime.now() - start_time)
