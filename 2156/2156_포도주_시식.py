import sys
sys.stdin = open('2156_포도주_시식.txt')

n = int(input())
wine_info = [int(input()) for _ in range(n)]

tasting = [[0 for _ in range(3)] for _ in range(n)]
tasting[0][1] = wine_info[0]
tasting[0][2] = wine_info[0]

for i in range(1, n):
    tasting[i][0] = max(tasting[i - 1])
    for j in range(2):
        tasting[i][j + 1] = tasting[i - 1][j] + wine_info[i]
print(max(tasting[-1]))
