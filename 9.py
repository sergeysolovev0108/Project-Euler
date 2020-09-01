"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

a = 1
b = 2
c = 3

for a in range(200, 400):
    for b in range(200, 400):
        for c in range(400, 700):
            if a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000 and a < b < c:
                print(a, b, c)
                break
