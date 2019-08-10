x = [[1, 2],
     [34, 45],
     [23,54]]


mul = [[0, 0, 0],
       [0, 0, 0]]

for i in range(len(x)):
    for j in range(len(x[0])):

        mul[j][i] = x[i][j]

for i in mul:

    print(i)

