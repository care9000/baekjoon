import sys
sys.stdin = open('1.txt')


def dfs(location, cnt, type):
    global min_cnt
    if cnt > 10:
        return

    for i in range(N):
        if 1 not in mini_map[i]:
            if cnt < min_cnt:
                min_cnt = cnt

    tem_location = []
    print(location)
    [print(mini_map[i]) for i in range(N)]
    for tem in location:
        tem_location.append(tem[:])

    if type == 0:
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if is_ok(nx, ny, k):
                work(nx, ny, k)
                tem_location = [[nx, ny], [nx + dx[k], ny + dy[k]]]
                dfs(tem_location, cnt + 1, (k % 2) + 1)
                dework(nx, ny, k)

    elif type == 1:
        tem_location = sorted(tem_location)
        for k in range(4):
            if k == 0:
                if -1 < tem_location[0][1] - 1 < M and mini_map[tem_location[0][0][tem_location[0][1] - 1] > 0 and visited[]]:









def is_ok(i, j, k):
    for l in range(2):
        if -1 < i + l * dx[k] < N and -1 < j + l * dy[k] < M and mini_map[i + l * dx[k]][j + l * dy[k]] > 0 and visited[i + l * dx[k]][j + l * dy[k]] < 4:
            pass
        return False

    return True


def work(i, j, k):
    for l in range(2):
        mini_map[i + l * dx[k]][j + l * dy[k]] = 2
        visited[i + l * dx[k]][j + l * dy[k]] += 1


def dework(i, j, k):
    for l in range(2):
        mini_map[i + l * dx[k]][j + l * dy[k]] = 1
        visited[i + l * dx[k]][j + l * dy[k]] -= 1


N, M = map(int, input().split())
mini_map = [list(map(int, input().split())) for _ in range(N)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

min_cnt = 11
for i in range(N):
    for j in range(M):
        if mini_map[i][j] == 1:
            visited = [[0 for _ in range(M)] for _ in range(N)]
            location = [[i, j]]
            visited[i][j] = 1
            mini_map[i][j] = 2
            dfs(location, 1, 0)
            visited[i][j] = 0
            mini_map[i][j] = 1
            for k in range(2, 4):
                nx = i + dx[k]
                ny = j + dy[k]
                if -1 < nx < N and -1 < ny < M and mini_map[nx][ny] == 1:
                    visited[i][j], visited[nx][ny] = 1, 1
                    mini_map[i][j] = mini_map[nx][ny] = 2
                    location = [[i, j], [nx, ny]]
                    dfs(location, 1, k)
                    mini_map[i][j] = mini_map[nx][ny] = 1
                    visited[i][j] = visited[nx][ny] = 0