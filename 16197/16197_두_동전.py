import sys
sys.stdin = open('16197_두_동전.txt')


def dfs(depth, i1, j1, i2, j2):
    global min_try

    if depth >= min_try:
        return

    for k in range(4):
        nx1 = i1 + dx[k]
        nx2 = i2 + dx[k]
        ny1 = j1 + dy[k]
        ny2 = j2 + dy[k]
        if ispass(nx1, ny1) and ispass(nx2, ny2):
            if is_go(nx1, ny1):
                pass
            else:
                nx1 = i1
                ny1 = j1
            if is_go(nx2, ny2):
                pass
            else:
                nx2 = i2
                ny2 = j2
            dfs(depth + 1, nx1, ny1, nx2, ny2)

        else:
            if ispass(nx1, ny1) or ispass(nx2, ny2):
                min_try = depth
            else:
                pass


def is_go(i, j):
    if mini_map[i][j] == '.':
        return True

    return False


def ispass(i, j):
    if -1 < i < N and -1 < j < M:
        return True

    return False


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
mini_map = [list(input()) for _ in range(N)]
coins = []
for i in range(N):
    for j in range(M):
        if mini_map[i][j] == 'o':
            coins.append([i, j])
            mini_map[i][j] = '.'


min_try = 11
dfs(1, coins[0][0], coins[0][1], coins[1][0], coins[1][1])
print(min_try if min_try < 11 else -1)