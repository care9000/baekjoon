import sys
sys.stdin = open('6087_레이저_통신.txt')


import collections


def bfs(i, j):
    q = collections.deque([])
    # (i, j) 좌표, 현재방향, 이때까지 꺾은 방향
    for k in range(4):
        q.append([i, j, k, 0])

    while len(q):
        i, j, dir, cnt = q.popleft()
        tem = dir

        tem += 4
        # 3방향 탐색
        for k in range(-1, 2, 1):
            i_tem = i + dx[(tem + k) % 4]
            j_tem = j + dy[(tem + k) % 4]

            if ispass(i_tem, j_tem):
                # cnt + 1 해줄것
                if k != 0:
                    if visited[i_tem][j_tem] >= cnt + 1:
                        visited[i_tem][j_tem] = cnt + 1
                        q.append([i_tem, j_tem, (tem + k) % 4, cnt + 1])

                else:
                    if visited[i_tem][j_tem] >= cnt:
                        visited[i_tem][j_tem] = cnt
                        q.append([i_tem, j_tem, dir, cnt])


def ispass(i, j):
    if -1 < i < H and -1 < j < W and mini_map[i][j] != 1:
        return True
    return False




dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

W, H = map(int, input().split())
dummy = list(input() for _ in range(H))

mini_map = [[0 for _ in range(W)] for _ in range(H)]
visited = [[987654321 for _ in range(W)] for _ in range(H)]
laser = []
#미니맵 만들기
for i in range(H):
    for j in range(W):
        if dummy[i][j] == '.':
            mini_map[i][j] = 0
        elif dummy[i][j] == '*':
            mini_map[i][j] = 1
        else:
            mini_map[i][j] = 9
            laser.append([i, j])
# 레이저에서 시작
laser_start_i = laser[0][0]
laser_start_j = laser[0][1]

laser_finish_i = laser[1][0]
laser_finish_j = laser[1][1]

bfs(laser_start_i, laser_start_j)
print(visited[laser_finish_i][laser_finish_j])
