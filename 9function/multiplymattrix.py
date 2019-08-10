x = [[1, 2, 3],
     [34, 45, 8],
     [37, 86, 69]]

y = [[10, 11, 12],
     [12, 18, 15],
     [13, 57, 78]]

mul = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]

for i in range(len(x)):
    for j in range(len(x[0])):

        mul[i][j] = x[i][j] * y[i][j]

for i in mul:
    print(i)