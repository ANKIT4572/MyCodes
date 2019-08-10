

x = [[1, 2, 3],
     [34, 45, 8],
     [37, 86, 69]]

y = [[10, 11, 12],
     [12, 18, 15],
     [13, 57, 78]]

sum = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]

for i in range(len(x)):
    for j in range(len(x[0])):

        sum[i][j] = x[i][j] + y[i][j]

for i in sum:
    print(i)

