R1 = [[1, 0.3, 0.4, 0.5, 0.1],
      [0.3, 1, 0.7, 0.3, 0.7],
      [0.9, 0, 1, 0.9, 0.7],
      [0.3, 0.5, 0.6, 1, 0.4],
      [0.2, 0.5, 0.7, 0.9, 1]]

R2 = [[1, 0, 1, 0, 0.6],
      [1, 1, 0.9, 0.4, 1],
      [0, 0.7, 1, 0, 0.7],
      [0.5, 0.3, 0, 1, 0.7],
      [1, 0.9, 0.8, 0.3, 1]]

lambda1 = 0.5
lambda2 = 0.5

Q1 = []
for i in range(5):
    row = []
    for j in range(5):
        row.append(min(R1[i][j]*lambda1, R2[i][j]*lambda2))
    Q1.append(row)

Q1s = []
for i in range(5):
    row = []
    for j in range(5):
        if Q1[i][j] >= Q1[j][i]:
            row.append(Q1[i][j] - Q1[j][i])
        else:
            row.append(0)
    Q1s.append(row)

Q1nd = []
for i in range(5):
    Q1nd.append(1 - max(Q1s[i]))

Q2 = []
for i in range(5):
    row = []
    for j in range(5):
        row.append(lambda1*R1[i][j] + lambda2*R2[i][j])
    Q2.append(row)

Q2s = []
for i in range(5):
    row = []
    for j in range(5):
        if Q2[i][j] >= Q2[j][i]:
            row.append(Q2[i][j] - Q2[j][i])
        else:
            row.append(0)
    Q2s.append(row)

Q2nd = []
for i in range(5):
    Q2nd.append(1 - max(Q2s[i]))

Q = []
for i in range(5):
    Q.append(min(Q1nd[i], Q2nd[i]))

print(Q)