import sys
sys.stdin = open('4179_불!.txt')
import collections

def fire_simulation():
    tem_fire_list = []
    while len(fire_list):
        i, j = fire_list.popleft()
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if ispass(nx, ny):
                tem_fire_list.append([nx, ny])
                mini_map[nx][ny] = 9

    for fire in tem_fire_list:
        fire_list.append([fire[0], fire[1]])


def jihoon_simulation():
    global flag
    tem_jihoon_list = []
    while len(jihoon_list):
        i, j = jihoon_list.popleft()
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if ispass(nx, ny) and mini_map[nx][ny] != 9 and vis[nx][ny] == 0:
                if nx == R - 1 or nx == 0 or ny == C -1 or ny == 0:
                    flag = 1
                    return
                tem_jihoon_list.append([nx, ny])
                vis[nx][ny] = 1

    for jihoon in tem_jihoon_list:
        jihoon_list.append([jihoon[0], jihoon[1]])


def ispass(i, j):
    if -1 < i < R and -1 < j < C and mini_map[i][j] == 0:
        return True

    return False

def isnotexit():
    for exit in exit_list:
        if mini_map[exit[0]][exit[1]] == 0:
            return False

    return True



dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


R, C = map(int, input().split())

dummy = [input() for _ in range(R)]

mini_map = [[0 for _ in range(C)] for _ in range(R)]

fire_list = collections.deque([])
jihoon_list = collections.deque([])
exit_list = collections.deque([])
for i in range(R):
    for j in range(C):
        if dummy[i][j] == 'F':
            fire_list.append([i, j])
            mini_map[i][j] = 9

        elif dummy[i][j] == 'J':
            jihoon_list.append([i, j])

        elif dummy[i][j] == '#':
            mini_map[i][j] = 1

        if dummy[i][j] != '#' and dummy[i][j] != 'F' and (i == R - 1 or i == 0 or j == C - 1 or j == 0):
            exit_list.append([i, j])

if len(exit_list) == 0:
    print('IMPOSSIBLE ')

else:
    flag = 0
    for exit in exit_list:
        if exit[0] == jihoon_list[0][0] and exit[1] == jihoon_list[0][1]:
            print(1)
            flag = 1
    vis = [[0 for _ in range(C)] for _ in range(R)]
    if flag == 0:
        time = 1
        while 1:
            fire_simulation()
            jihoon_simulation()
            if flag == 1:
                time += 1
                break
            if isnotexit() or len(jihoon_list) == 0 :
                time = - 1
                break
            time += 1
        print(time if time != -1 else 'IMPOSSIBLE ')




