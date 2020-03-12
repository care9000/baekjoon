import sys
sys.stdin = open('3987_보이저_1호.txt')


def bfs(dir):
    i, j, time = PR - 1, PC - 1, 0
    while 1:
        vis[i][j][dir] = 1
        nx = i + dx[dir]
        ny = j + dy[dir]
        if ispass(nx, ny):
            if vis[nx][ny][dir] == 1:
                return 987654321
            vis[nx][ny][dir] = 1

            if mini_map[nx][ny] == '/':
                if dir % 2 == 0:
                    dir = (dir + 5) % 4

                else:
                    dir = (dir + 3) % 4

            elif mini_map[nx][ny] == "\\":
                if dir % 2 == 0:
                    dir = (dir + 3) % 4

                else:
                    dir = (dir + 5) % 4

        else:
            return time + 1
        i = nx
        j = ny
        time += 1


def ispass(i, j):
    if -1 < i < N and -1 < j < M and mini_map[i][j] != 'C':
        return True
    return False

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
mini_map = [list(input()) for _ in range(N)]
PR, PC = map(int, input().split())

vis = [[[0 for _ in range(4)] for _ in range(M)] for _ in range(N)]


dir = 0
result_time = 0
for k in range(4):
    vis = [[[0 for _ in range(4)] for _ in range(M)] for _ in range(N)]
    tem_time = bfs(k)
    if tem_time > result_time:
        dir = k
        result_time = tem_time
        if result_time == 987654321:
            break
result_dir = ['U', 'R', 'D', 'L']

print(result_dir[dir])
print(result_time if result_time != 987654321 else 'Voyager')