import sys
sys.stdin = open('10972_다음_순열.txt')


def Perm(N, m):
    if N == m:
        result.append(data[:])
    else:
        for i in range(m, N):
            data[i], data[m] = data[m], data[i]
            Perm(N, m + 1)
            data[i], data[m] = data[m], data[i]


N = int(input())
sample = list(map(int, input().split()))

data = []
for i in range(1, N + 1):
    data.append(i)

result = []
Perm(N, 0)

result = sorted(result)
for i in range(len(result)):
    if result[i] == sample and i != len(result) - 1:
        for j in range(len(result[i])):
            print(result[i + 1][j], end=" ")
    elif result[i] == sample:
        print(-1)
