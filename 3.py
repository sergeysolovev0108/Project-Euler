"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


import math
from datetime import datetime

start_time = datetime.now()


def is_simple(a):
    res = math.ceil(math.sqrt(a))
    largest_prime_factor = 0
    for i in range(3, res):
        if a % i == 0:
            if not is_simple(i):
                largest_prime_factor = i
    return largest_prime_factor


x = is_simple(600851475143)
print(x)
print('ВРЕМЯ ВЫПОЛНЕНИЯ', datetime.now() - start_time)






