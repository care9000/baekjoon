import sys
sys.stdin = open('10844_쉬운_계단_수.txt')

N = int(input())

data = [[0 for _ in range(10)] for _ in range(N)]
data[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(1, N):
    data[i][0] = data[i - 1][1]
    for j in range(1, 9):
        data[i][j] = data[i - 1][j - 1] + data[i - 1][j + 1]
    data[i][9] = data[i - 1][8]
print(sum(data[-1]) % 1000000000)
