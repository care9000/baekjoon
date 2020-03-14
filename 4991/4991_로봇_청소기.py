import sys
import collections
sys.stdin = open('4991_로봇_청소기.txt')


def dp():
    global distance
    tem = 0
    for i in range(len(info) - 1):
        if 0 < dis[info[i]][info[i + 1]]:
            tem += dis[info[i]][info[i + 1]]
        elif -1 == dis[info[i]][info[i + 1]]:
            return
    if tem != 0 and distance > tem:
        distance = tem


def Pem(n, m):
    if n == m:
        dp()
        return
    else:
        for k in range(m, n):
            info[k], info[m] = info[m], info[k]
            Pem(n, m + 1)
            info[k], info[m] = info[m], info[k]


def bfs(i, j, point):
    q = collections.deque([])
    q.append([i, j, 0])
    vis[i][j] = 1
    while len(q):
        i, j, time = q.popleft()
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if ispass(nx, ny) and vis[nx][ny] != 1:
                vis[nx][ny] = 1
                if 0 < mini_map[nx][ny] < 11:
                    dis[point][mini_map[nx][ny]] = time + 1

                q.append([nx, ny, time + 1])


def ispass(i, j):
    if -1 < i < h and -1 < j < w and mini_map[i][j] != 11:
        return True

    return False


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while 1:
    w, h = map(int, input().split())
    if w == 0:
        break
    mini_map = [[0 for _ in range(w)] for _ in range(h)]
    work = 0
    work_place = collections.deque([])
    start = []
    for H in range(h):
        dummy = list(input())
        for W in range(w):
            if dummy[W] == 'o':
                start.append(H)
                start.append(W)
                mini_map[H][W] = 0

            elif dummy[W] == '*':
                work += 1
                mini_map[H][W] = work
                work_place.append([H, W])

            elif dummy[W] == 'x':
                mini_map[H][W] = 11

            else:
                continue

    dis = [[-1 for _ in range(work + 1)] for _ in range(work + 1)]
    vis = [[0 for _ in range(w)] for _ in range(h)]
    bfs(start[0], start[1], 0)
    for k in range(work):
        vis = [[0 for _ in range(w)] for _ in range(h)]
        bfs(work_place[k][0], work_place[k][1], k + 1)

    info = collections.deque([i for i in range(1, work + 1)])
    info.appendleft(0)
    distance = 987654321
    Pem(work + 1, 1)
    print(distance if distance != 987654321 else -1)