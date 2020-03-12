import sys
sys.stdin = open('3197_백조의 호수.txt')
import collections

def melt():
    while len(lakes):
        i, j = lakes.popleft()
        mini_map[i][j] = '.'
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if ispass(nx, ny) and vis[nx][ny] == 0:
                if mini_map[nx][ny] == 'X':
                    vis[nx][ny] = 1
                    next_lakes.append([nx, ny])
                else:
                    lakes.append([nx, ny])
                    vis[nx][ny] = 1


def bfs():
    global flag
    while len(swan_extend):
        i, j = swan_extend.popleft()
        if i == swan[2] and j == swan[3]:
            return True
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if ispass(nx, ny) and vis[nx][ny] == 0:
                if mini_map[nx][ny] == '.':
                    vis[nx][ny] = 1
                    swan_extend.append([nx, ny])
                else:
                    next_q.append([nx, ny])
                    vis[nx][ny] = 1


def ispass(i, j):
    if -1 < i < R and -1 < j < C:
        return True

    return False


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


R, C = map(int, input().split())
mini_map = [[0] * C for _ in range(R)]
swan = []
swan_extend = collections.deque([])
lakes = collections.deque([])
vis = [[0 for _ in range(C)] for _ in range(R)]
for r in range(R):
    for c, d in enumerate(list(sys.stdin.readline().replace("\n", ""))):
        mini_map[r][c] = d
        if mini_map[r][c] == 'L':
            swan.append(r)
            swan.append(c)
            mini_map[r][c] = '.'
        if mini_map[r][c] == '.':
            lakes.append([r, c])
            vis[r][c] = 1


swan_extend.append([swan[0], swan[1]])
vis[swan[0]][swan[1]] = 1
time = 0
next_q = collections.deque([])
next_lakes = collections.deque([])
while 1:
    melt()
    flag = 0
    if bfs():
        print(time)
        break
    swan_extend = next_q
    lakes = next_lakes
    next_q = collections.deque([])
    next_lakes = collections.deque([])
    time += 1

