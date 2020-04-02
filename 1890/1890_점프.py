import sys
sys.stdin = open('1890_점프.txt')
input = sys.stdin.readline
def dfs(i, j):
    if i == N - 1 and j == N - 1:
        return 1
    if dp[i][j] != -1:
        return dp[i][j]
    jump = mini_map[i][j]
    dp[i][j] = 0
    for k in range(2):
        nx = i + (dx[k] * jump)
        ny = j + (dy[k] * jump)
        if ispass(nx, ny):
            dp[i][j] += dfs(nx, ny)

    return dp[i][j]


def ispass(i, j):
    if -1 < i < N and -1 < j < N:
        return True

    return False


# 아래 오른쪽
dx = [1, 0]
dy = [0, 1]

N = int(input())
mini_map = []
dp = []
for _ in range(N):
    data = list(map(int, input().split()))
    mini_map.append(data)
    dp.append([-1 for _ in range(N)])

print(dfs(0, 0))