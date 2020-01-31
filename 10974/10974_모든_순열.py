import sys
sys.stdin = open('10974_모든_순열.txt')

def Perm(N, m):
    if N == m:
        result.append(data[:])
    else:
        for i in range(m, N):
            data[m], data[i] = data[i], data[m]
            Perm(N, m + 1)
            data[m], data[i] = data[i], data[m]



N = int(input())

data = []
for i in range(1, N + 1):
    data.append(i)
result = []

Perm(N, 0)
result = sorted(result)
for i in range(len(result)):
    for j in range(len(result[i])):
        print(result[i][j], end=" ")
    print()
