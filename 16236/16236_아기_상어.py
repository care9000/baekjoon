import sys
sys.stdin = open('16236_아기_상어.txt')
import collections

def simulation(i, j):
    global check, dist, eaten
    q = collections.deque([])
    q.append([i, j, dist])
    visited[i][j] = 1
    while len(q):
        i, j, cnt = q.popleft()
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if ispass(nx, ny) and visited[nx][ny] == 0:
                if 0 < mini_map[nx][ny] < shark_level:
                    visited[nx][ny] = 1
                    foods.append([nx, ny, cnt + 1])
                    check = 1

                elif mini_map[nx][ny] == 0 or mini_map[nx][ny] == shark_level:
                    visited[nx][ny] = 1
                    q.append([nx, ny, cnt + 1])


def ispass(i, j):
    if -1 < i < N and -1 < j < N:
        return True
    return False


dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


N = int(input())

mini_map = [list(map(int, input().split())) for _ in range(N)]
fishes = [0 for _ in range(7)]
shark_location = [0, 0]
for i in range(N):
    for j in range(N):
        if mini_map[i][j] and mini_map[i][j] != 9:
            fishes[mini_map[i][j]] += 1
        elif mini_map[i][j] == 9:
            shark_location[0] = i
            shark_location[1] = j
            mini_map[i][j] = 0


shark_level = 2
eaten = 0
check = 0
dist = 0
while 1:
    check = 0
    # print(shark_location, dist, shark_level)
    foods = []
    if eaten == shark_level:
        shark_level += 1
        eaten = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]
    simulation(shark_location[0], shark_location[1])
    if check == 0:
        break

    else:
        h = 987654321
        w = 987654321
        tem = 987654321
        for food in foods:
            if tem > food[2]:
                h = food[0]
                w = food[1]
                dist = food[2]
                tem = food[2]
            elif tem == food[2] and food[0] < h:
                h = food[0]
                w = food[1]
                dist = food[2]
                tem = food[2]
            elif tem == food[2] and h == food[0] and food[1] < w:
                h = food[0]
                w = food[1]
                dist = food[2]
                tem = food[2]
        mini_map[h][w] = 0
        eaten += 1
        shark_location[0] = h
        shark_location[1] = w


print(dist)