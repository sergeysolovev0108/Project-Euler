"""
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
What is the value of this product?
"""


def multiply(lst):
    x = 1
    for i in lst:
        x *= i
    return x


with open('8.txt') as file:
    num = list(map(int, ''.join(i.strip() for i in file)))

product_of_numbers = 0

for i in range(len(num) - 12):
    temp = multiply(num[i:i + 13])
    if temp > product_of_numbers:
        product_of_numbers = temp

print(product_of_numbers)

