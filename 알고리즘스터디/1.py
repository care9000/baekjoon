import sys
sys.stdin = open('1.txt')

def dfs(i, j, cnt, type):
    if cnt > min_cnt:
        return

    for k in range(4):
        if type == 0:
            if is_type_1or2(i, j, k):
                work(i, j, k)
                dfs(cnt, type)
                dework(i, j, k)

def work(i, j, k):
    for x in range(1, 3):
        for y in range(1, 3):
            mini_map[i + (dx[k] * x)][j + (dy[k] * y)] = 0
            visited[i + (dx[k] * x)][j + (dy[k] * y)] += 1


def dework(i, j, k):
    for x in range(1, 3):
        for y in range(1, 3):
            mini_map[i + (dx[k] * x)][j + (dy[k] * y)] = 1
            visited[i + (dx[k] * x)][j + (dy[k] * y)] -= 0


def is_type_1or2(i, j, k):
    for x in range(1, 3):
        for y in range(1, 3):
            if -1 < i + (dx[k] * x) < N and -1 < j + (dy[k] * y) < M and visited[i + (dx[k] * x)][j + (dy[k] * y)] < 4 and mini_map[i + (dx[k] * x)][j + (dy[k] * y)] == 1:
                pass
            else:
                return False
    return True



dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N, M = map(int, input().split())

now_location = [[0, 0], [0, 0]]
mini_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
min_cnt = 11

for i in range(N):
    for j in range(M):
        if mini_map[i][j] == 1:
            for k in range(3):
                if k == 0:
                    visited = [[0 for _ in range(M)] for _ in range(N)]
                    now_location[0][0] = i
                    now_location[0][1] = j
                    now_location[1][0] = i
                    now_location[1][1] = j
                    mini_map[i][j] = 0
                    visited[i][j] = 1
                    dfs(i, j, 1, k)
                    mini_map[i][j] = 1
                    visited[i][j] -= 1
                #가로 위치
                elif k == 1:
                    if -1 < j + 1 < M and mini_map[i][j + 1]:
                        visited = [[0 for _ in range(M)] for _ in range(N)]
                        now_location[0][0] = i
                        now_location[0][1] = j
                        now_location[1][0] = i
                        now_location[1][1] = j + 1
                        mini_map[i][j] = 0
                        visited[i][j] = 1
                        mini_map[i][j + 1] = 0
                        visited[i][j + 1] = 1
                        dfs(i, j, 1, k)
                        mini_map[i][j] = 1
                        visited[i][j] = 0
                        mini_map[i][j + 1] = 1
                        visited[i][j + 1] = 0
                #세로위치
                else:
                    if -1 < i + 1 < M and mini_map[i + 1][j]:
                        visited = [[0 for _ in range(M)] for _ in range(N)]
                        now_location[0][0] = i
                        now_location[0][1] = j
                        now_location[1][0] = i + 1
                        now_location[1][1] = j
                        mini_map[i][j] = 0
                        visited[i][j] = 1
                        mini_map[i + 1][j] = 0
                        visited[i + 1][j] = 1
                        dfs(i, j, 1, k)
                        mini_map[i][j] = 1
                        visited[i][j] = 0
                        mini_map[i + 1][j] = 1
                        visited[i + 1][j] = 0

