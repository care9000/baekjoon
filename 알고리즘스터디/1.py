import sys
sys.stdin = open('1.txt')

def simulation(i, j, type, cnt):
    global min_cnt
    if cnt >= min_cnt:
        return

    if is_check():
        if cnt < min_cnt:
            min_cnt = cnt

    #새워 졌을 떄
    if type == 0:
        for k in range(4):
            if k == 0 or k == 3:
                nx = i + dx[k]
                ny = j + dy[k]
                # 상, 하 일 때
                if k % 2 == 0:
                    if is_2_type(nx, ny):
                        type_2_work(nx, ny)
                        simulation(nx, ny, 2, cnt + 1)
                        type_2_dework(nx, ny)
                else:
                    if is_1_type(nx, ny):
                        type_1_work(nx, ny)
                        simulation(nx, ny, 1, cnt + 1)
                        type_1_dework(nx, ny)
            else:
                nx = i + roll_dx[k]
                ny = j + roll_dy[k]
                # 상, 하 일 때
                if k % 2 == 0:
                    if is_2_type(nx, ny):
                        type_2_work(nx, ny)
                        simulation(nx, ny, 2, cnt + 1)
                        type_2_dework(nx, ny)
                else:
                    if is_1_type(nx, ny):
                        type_1_work(nx, ny)
                        simulation(nx, ny, 1, cnt + 1)
                        type_1_dework(nx, ny)

    elif type == 1:
        for k in range(4):
            if k % 2 == 0:
                nx = i + roll_dx[k]
                ny = j + roll_dy[k]
                if is_1_type(nx, ny):
                    type_1_work(nx, ny)
                    simulation(nx, ny, 1, cnt + 1)
                    type_1_dework(nx, ny)

            elif k == 1:
                nx = i + dx[k]
                ny = j + dy[k]
                if is_0_type(nx, ny):
                    type_0_work(nx, ny)
                    simulation(nx, ny, 0, cnt + 1)
                    type_0_dework(nx, ny)
            elif k == 3:
                nx = i + roll_dx[k]
                ny = j + roll_dy[k]
                if is_0_type(nx, ny):
                    type_0_work(nx, ny)
                    simulation(nx, ny, 0, cnt + 1)
                    type_0_dework(nx, ny)

    elif type == 2:
        for k in range(4):
            if k % 2 == 1:
                nx = i + roll_dx[k]
                ny = j + roll_dy[k]
                if is_2_type(nx, ny):
                    type_2_work(nx, ny)
                    simulation(nx, ny, 2, cnt + 1)
                    type_2_dework(nx, ny)

            elif k == 2:
                nx = i + dx[k]
                ny = j + dy[k]
                if is_0_type(nx, ny):
                    type_0_work(nx, ny)
                    simulation(nx, ny, 0, cnt + 1)
                    type_0_dework(nx, ny)
            elif k == 0:
                nx = i + roll_dx[k]
                ny = j + roll_dy[k]
                if is_0_type(nx, ny):
                    type_0_work(nx, ny)
                    simulation(nx, ny, 0, cnt + 1)
                    type_0_dework(nx, ny)



def is_check():
    for i in range(N):
        for j in range(M):
            if mini_map[i][j] == 1:
                if visited[i][j] == 0:
                    return False

    return True


def is_2_type(i, j):
    for k in range(2):
        if -1 < i + k < N and -1 < j < M:
            if mini_map[i + k][j] > 0 and visited[i + k][j] < 4:

                pass
            else:
                return False
        else:
            return False
    return True

def is_1_type(i, j):
    for k in range(2):
        if -1 < j + k < M and mini_map[i][j + k] > 0 and visited[i][j + k] < 4:
            pass

        else:
            return False

    return True



def is_0_type(i, j):
    if -1 < i < N and -1 < j < M:
        if visited[i][j] < 4 and mini_map[i][j] > 0:
            return True

    return False

def type_0_work(i, j):
    mini_map[i][j] = 2
    visited[i][j] += 1


def type_0_dework(i, j):
    mini_map[i][j] = 1
    visited[i][j] -= 1


def type_1_work(i, j):
    mini_map[i][j] = 2
    mini_map[i][j + 1] = 2
    visited[i][j] += 1
    visited[i][j + 1] += 1


def type_1_dework(i, j):
    mini_map[i][j] = 1
    mini_map[i][j + 1] = 1
    visited[i][j] -= 1
    visited[i][j + 1] -= 1


def type_2_work(i, j):
    mini_map[i][j] = 2
    mini_map[i + 1][j] = 2
    visited[i][j] += 1
    visited[i + 1][j] += 1

def type_2_dework(i, j):
    mini_map[i][j] = 1
    mini_map[i + 1][j] = 1
    visited[i][j] -= 1
    visited[i + 1][j] -= 1


dx = [-2, 0, 2, 0]
dy = [0, 2, 0, -2]

roll_dx = [-1, 0, 1, 0]
roll_dy = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    mini_map = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0 for _ in range(M)] for _ in range(N)]
    min_cnt = 11
    for i in range(N - 1 , -1, -1):
        for j in range(M - 1, -1, -1):
            if mini_map[i][j] == 1:
                # 타입 0는 방향이 필요 없음.
                if is_0_type(i, j):
                    type_0_work(i, j)
                    # i 좌표 j 좌표 모양, cnt
                    simulation(i, j, 0, 1)
                    type_0_dework(i, j)

                if is_1_type(i, j):
                    type_1_work(i, j)
                    simulation(i, j, 1, 1)
                    type_1_dework(i, j)
                if is_2_type(i, j):
                    type_2_work(i, j)
                    simulation(i, j, 2, 1)
                    type_2_dework(i, j)
    if min_cnt == 11:
        min_cnt = -1
    print("#{} {}".format(tc, min_cnt))