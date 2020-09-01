"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and
115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""

nums = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    15: 'fifteen',
    18: 'eighteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    }


def generate_number(number, dict_of_numbers):
    temp=''
    x = str(number)
    if dict_of_numbers.get(number, False):
        return dict_of_numbers[number]
    elif number < 20:
        return dict_of_numbers[int(x[1])] + 'teen'
    elif number < 100:
        temp = number - int(x[1])
        return dict_of_numbers[temp] + dict_of_numbers[int(x[1])]
    elif number < 1000:
        if x[1:3] == '00':
            return dict_of_numbers[int(x[0])] + 'hundred'
        else:
            return dict_of_numbers[int(x[0])] + 'hundredand' + generate_number(int(x[1:3]), nums)
    elif number == 1000:
        return 'onethousand'


sum_of_numbers = 0
for i in range(1, 1001):
    sum_of_numbers += len(generate_number(i, nums))
    #  print(i, ':', generate_number(i, nums))
print(sum_of_numbers, 'letters used')