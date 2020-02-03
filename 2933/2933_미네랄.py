import sys
import collections
sys.stdin = open('2933_미네랄.txt')


def simulation():
    global location
    cnt = 0
    while len(attemp) > cnt:

        destroy = attemp[cnt]
        destroy = R - destroy
        if 1 not in mini_map[destroy]:
            pass
        else:
            find_mineral(destroy, cnt % 2)
            for k in range(4):
                i_tem = destroy + dx[k]
                j_tem = location + dy[k]
                if ispass(i_tem, j_tem) and mini_map[i_tem][j_tem] == 1:
                    if is_gravity(i_tem, j_tem):
                        break

        cnt += 1



def find_mineral(destroy, dir):
    global location
    if dir == 0:
        for i in range(C):
            if mini_map[destroy][i] == 1:
                mini_map[destroy][i] = 0
                location = i
                return
    else:
        for i in range(C - 1, -1, -1):
            if mini_map[destroy][i] == 1:
                mini_map[destroy][i] = 0
                location = i
                return


def is_gravity(i, j):
    vis = [[0 for _ in range(C)] for _ in range(R)]
    q = collections.deque([])
    i_start = i
    j_start = j
    vis[i_start][j_start] = 1
    q.append([i_start, j_start])
    while len(q):
        i, j = q.popleft()
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if ispass(nx, ny) and vis[nx][ny] == 0 and mini_map[nx][ny] == 1:
                vis[nx][ny] = 1
                q.append([nx, ny])
    if 1 not in vis[-1]:
        for x in range(R):
            for y in range(C):
                if vis[x][y] == 1:
                    mini_map[x][y] = 0
        is_check(vis)
        return True
    return False



def is_check(vis):
    if 1 in vis[-1]:
        change(vis)
        return
    else:
        for x in range(R - 2, -1, -1):
            for y in range(C):
                if vis[x][y] == 1:
                    if mini_map[x + 1][y] == 1:
                        change(vis)
                        return

    gravity(vis)


def gravity(vis):
    for i in range(R - 2, -1, -1):
        for j in range(C):
            vis[i + 1][j] = vis[i][j]
            vis[i][j] = 0
    is_check(vis)



def change(vis):
    for x in range(R):
        for y in range(C):
            if vis[x][y] == 1:
                mini_map[x][y] = 1




def ispass(i, j):
    if -1 < i < R and -1 < j < C:
        return True

    return False


dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

R, C = map(int, sys.stdin.readline().split())
dummy = [input() for _ in range(R)]

N = int(input())
attemp = list(map(int, sys.stdin.readline().split()))
mini_map = [[0 for _ in range(C)] for _ in range(R)]
for i in range(R):
    for j in range(C):
        if dummy[i][j] == 'x':
            mini_map[i][j] = 1

location = -1
simulation()
for i in range(R):
    for j in range(C):
        if mini_map[i][j] == 1:
            print('x', end="")
        else:
            print('.', end="")
    print()
