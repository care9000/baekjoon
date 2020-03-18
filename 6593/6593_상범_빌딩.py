import sys
sys.stdin = open('6593_상범_빌딩.txt')
import collections


def bfs(i, j, k):
    q = collections.deque([])
    q.append([i, j, k, 0])
    vis[i][j][k] = 1
    while len(q):
        i, j, k, time = q.popleft()
        for move in range(6):
            nx = j + dx[move]
            ny = k + dy[move]
            nz = i + dz[move]
            if ispass(nz, nx, ny) and vis[nz][nx][ny] == 0:
                if mini_map[nz][nx][ny] == 'E':
                    return time + 1
                vis[nz][nx][ny] = 1
                q.append([nz, nx, ny, time + 1])


def ispass(z, x, y):
    if -1 < z < L and -1 < x < R and -1 < y < C and mini_map[z][x][y] != '#':
        return True

    return False


dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

while 1:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break

    mini_map = []
    for i in range(L):
        tem = [input() for _ in range(R)]
        mini_map.append(tem)
        input()

    vis = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(L)]
    start = []
    end = []
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if mini_map[i][j][k] == 'S':
                    start.append([i, j, k])
                elif mini_map[i][j][k] == 'E':
                    end.append([i, j, k])

    result = bfs(start[0][0], start[0][1], start[0][2])
    if result == (None):
        print('Trapped!')
    else:
        print('Escaped in {} minute(s).'.format(result))


