"""The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million."""

from datetime import datetime
start_time = datetime.now()

length = 0
chains = []

for x in range(1, 1000000):
    temp = [x]
    while True:
        if x == 1:
            break
        if x % 2 == 0:
            x = x//2
            temp.append(x)
        if x % 2 != 0 and x != 1:
            x = ((3*x) + 1)
            temp.append(x)
    if len(temp) > len(chains):
        chains = temp

print('ЧИСЛО ', chains[0], 'ИМЕЕТ БОЛЬШЕ ВСЕГО ЧИСЕЛ В ПОСЛЕДОВАТЕЛЬНОСТИ', len(chains))
print(chains)
print('ВРЕМЯ ВЫПОЛНЕНИЯ', datetime.now() - start_time)
