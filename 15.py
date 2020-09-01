"""Starting in the top left corner of a 2×2 grid,
and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?"""

X = [[1 for j in range(20)] for i in range(21)]
for i in range(1, 21):
    for j in range(len(X[0])):
        X[i][j] = X[i][j-1] + X[i-1][j]
X.pop(0)
for routes in X:
    print(routes)
print('В сетке 20х20 существует', X[19][19], ' маршрутов прохождения')
