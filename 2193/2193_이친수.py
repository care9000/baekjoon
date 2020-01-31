import sys
sys.stdin = open('2193_이친수.txt')

N = int(input())
data = []
data.append(1)
data.append(2)
for i in range(1, N - 1):
    data.append(data[-1] + data[-2])
print(data[-2])