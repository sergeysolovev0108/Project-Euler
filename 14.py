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

chains = {key: 0 for key in range(1, 1000000)}
longest = 0
answer = 0

for number in range(1, 1000000):
    temp = number
    count = 1

    while temp > 1:
        if temp % 2 == 0:
            temp = temp / 2
        else:
            temp = 3 * temp + 1
        if temp in chains and chains[temp] != 0:
            count += chains[temp]
            break
        count += 1

    chains[number] = count
    if count > longest:
        longest = count
        answer = number

print('Number', answer, 'produces the longest chain')
print(chains[answer])
print('Time:', datetime.now() - start_time)
