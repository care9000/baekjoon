import sys
sys.stdin = open('13459_구슬_탈출.txt')


def dfs(red_i, red_j, blue_i, blue_j, cnt):
    red_i_start = red_i
    red_j_start = red_j
    if result != 11:
        return
    elif cnt > 10:
        return

    for k in range(4):
        for _ in range(10):
            red_i_tem = red_i_start + dx[k]
            red_j_tem = red_j_start + dy[k]
            if ispass(red_i_tem, red_j_tem):
                if mini_map[red_i_tem][red_j_tem] == 0:
                    mini_map[red_i_tem][red_j_tem] = 7
                    mini_map[red_i_start][red_j_start] = 0
                    red_i_start = red_i_tem
                    red_j_start = red_j_tem

                elif mini_map[red_i_tem][red_j_tem] == 9:
                    goal = 1






def ispass(i, j):
    if -1 < i < N and -1 < j < M:
        return True
    return False

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())

dummy = [input() for _ in range(N)]
mini_map = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if dummy[i][j] == 'R':
            mini_map[i][j] = 7

        elif dummy[i][j] == 'B':
            mini_map[i][j] = 8

        elif dummy[i][j] == 'O':
            mini_map[i][j] = 9

        elif dummy[i][j] == '#':
            mini_map[i][j] = 1




location = [[0, 0], [0, 0]]
for i in range(N):
    for j in range(M):
        if mini_map[i][j] == 'R':
            location[0][0] = i
            location[0][1] = j
        elif mini_map[i][j] == 'B':
            location[1][0] = i
            location[1][1] = j

result = 11
dfs(location[0][0], location[0][1], location[1][0], location[1][1], 0)