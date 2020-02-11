import sys
sys.stdin = open('13459_구슬_탈출.txt')


def dfs(red_i, red_j, blue_i, blue_j, cnt):
    global result

    red_start_i = red_i
    red_start_j = red_j
    blue_start_i = blue_i
    blue_start_j = blue_j
    goal = 0
    if cnt > 10:
        return
    elif result == 1:
        return

    for k in range(4):
        for _ in range(10):
            for a in range(2):
                if a == 0:
                    i_tem = red_i + dx[k]
                    j_tem = red_j + dy[k]
                    if -1 < i_tem < N and -1 < j_tem < M:
                        if mini_map[i_tem][j_tem] == 9:
                            goal += 1
                        elif mini_map[i_tem][j_tem] == 0:
                            mini_map[red_i][red_j] = 0
                            red_i = i_tem
                            red_j = j_tem
                            mini_map[i_tem][j_tem] = 7
                else:
                    pass
        if goal == 1:
            result = 1
            return
        elif goal > 1:
            return

        dfs(red_i, red_j, blue_i, blue_j, cnt + 1)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


N, M = map(int, input().split())
dummy = [input() for _ in range(N)]

mini_map = [[0 for _ in range(M)] for _ in range(N)]

#빨간 구슬 7 파란구술 8 골인지점 9
red_i = 0
red_j = 0

blue_i = 0
blue_j = 0
for i in range(N):
    for j in range(M):
        if dummy[i][j] == 'R':
            mini_map[i][j] = 7
            red_i = i
            red_j = j

        elif dummy[i][j] == 'B':
            mini_map[i][j] = 8
            blue_i = i
            blue_j = j

        elif dummy[i][j] == 'O':
            mini_map[i][j] = 9

        elif dummy[i][j] == '#':
            mini_map[i][j] = 1

result = 0
dfs(red_i, red_j, blue_i, blue_j, 0)