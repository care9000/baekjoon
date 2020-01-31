import sys
sys.stdin = open('11399_ATM.txt')

N = int(input())
P = list(map(int, input().split()))

P = sorted(P)
data = [0 for _ in range(N)]
for i in range(N):
    for j in range(i + 1):
        data[i] += P[j]
print(sum(data))