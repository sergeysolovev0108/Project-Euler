"""Work out the first ten digits of the sum of the following one-hundred 50-digit numbers."""

with open('13.txt') as file:
    num = file.read().splitlines()
sam = list((map(int, num)))
sam = str(sum(sam))
answer = int(sam[0:10])
print(answer)
