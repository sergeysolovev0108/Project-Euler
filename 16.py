"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""
from datetime import datetime
import numpy as np

start_time = datetime.now()

print(sum(int(i) for i in str(2**1000)))



a = list(x)
x = str(2**1000)

xc = np.array([int(x) for x in a])
v = np.sum(xc)

print(v, 'сумма из NumPy')
print('Time:', datetime.now() - start_time)
