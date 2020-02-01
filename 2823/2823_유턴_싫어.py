import sys
sys.stdin = open('2823_유턴_싫어.txt')

def dfs(i, j, dir):
    global flag
    if flag == 1:
        return

    for k in range(4):
        if dir == -1:
            nx = i + dx[k]
            ny = j + dy[k]
            if ispass(nx, ny) and visited[nx][ny] == 0 and mini_map[nx][ny] != 'X':
                visited[nx][ny] = 1
                if nx == road[0] and ny == road[1]:
                    flag = 1
                    return
                dfs(nx, ny, k)
                visited[nx][ny] = 0

        else:
            if (dir + 2) % 4 != k:
                nx = i + dx[k]
                ny = j + dy[k]
                if ispass(nx, ny) and visited[nx][ny] == 0 and mini_map[nx][ny] != 'X':

                    visited[nx][ny] = 1
                    if nx == road[0] and ny == road[1]:
                        flag = 1
                        return

                    dfs(nx, ny, k)
                    visited[nx][ny] = 0


def ispass(i, j):
    if -1 < i < R and -1 < j < C:
        return True

    return False

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

R, C = map(int, sys.stdin.readline().split())
mini_map = [input() for _ in range(R)]
buildings = []
roads = []
for i in range(R):
    for j in range(C):
        if mini_map[i][j] == 'X':
            buildings.append([i, j])
        else:
            roads.append([i, j])
result = 0

for road in roads:
    flag = 0
    visited = [[0 for _ in range(C)] for _ in range(R)]
    dfs(road[0], road[1], -1)

    if flag == 1:
        pass
    else:

        result = 1
        break

print(result)