import sys
sys.stdin = open('1520_내리막길.txt')
input = sys.stdin.readline

def dfs(i, j):
    if i == M - 1 and j == N - 1:
        return 1
    # 이미 왔었으면 더이상 할 필요 없음
    if dp[i][j] != -1:
        return dp[i][j]
    # 방문 했으면 방문 체크를 0으로 해줌
    dp[i][j] = 0
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if ispass(nx, ny) and mini_map[i][j] > mini_map[nx][ny]:
            dp[i][j] += dfs(nx, ny)
    return dp[i][j]


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
dp = [[-1 for _ in range(N)] for _ in range(M)]
dfs(0, 0)
print(dp[0][0])

