import sys
sys.stdin = open('1520_내리막길.txt')
import collections
input = sys.stdin.readline

def dfs(i, j):
    if i == M - 1 and j == N - 1:
        dp[i][j] += 1
        return
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if ispass(nx, ny) and mini_map[nx][ny] < mini_map[i][j]:
            dfs(nx, ny)


def ispass(i, j):
    if -1 < i < M and -1 < j < N:
        return True
    return False


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

M, N = map(int, input().split())
mini_map = []
for _ in range(M):
    data = list(map(int, input().split()))
    mini_map.append(data)
dp = [[0 for _ in range(N)] for _ in range(M)]
dp[0][0] = 1
dfs(0, 0)
print(dp[-1][-1])