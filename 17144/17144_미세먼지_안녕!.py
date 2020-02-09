import sys
sys.stdin = open('17144_미세먼지_안녕!.txt')

def down_simulation():
    i = location[1][0]
    j = location[1][1]
    dir = 2
    while 1:
        i_tem = i + dx[dir]
        j_tem = j + dy[dir]
        if down_iswall(i_tem, j_tem):
            i_tem = i + dx[(dir + 3) % 4]
            j_tem = j + dy[(dir + 3) % 4]
            dir += 3
            dir %= 4

        if mini_map[i_tem][j_tem] == -1:
            mini_map[i][j] = 0
            return

        elif mini_map[i][j] != -1 and mini_map[i_tem][j_tem] != -1:
                mini_map[i][j] = mini_map[i_tem][j_tem]

        i = i_tem
        j = j_tem


def up_simulation():
    i = location[0][0]
    j = location[0][1]
    dir = 0
    while 1:
        i_tem = i + dx[dir]
        j_tem = j + dy[dir]
        if up_iswall(i_tem, j_tem):
            i_tem = i + dx[(dir + 1) % 4]
            j_tem = j + dy[(dir + 1) % 4]
            dir += 1
            dir %= 4

        if mini_map[i_tem][j_tem] == -1:
            mini_map[i][j] = 0
            return

        elif mini_map[i][j] != -1 and mini_map[i_tem][j_tem] != -1:
                mini_map[i][j] = mini_map[i_tem][j_tem]

        i = i_tem
        j = j_tem


def diffusion():
    dusts = []
    # 미세 먼지가 있을 경우 dust에 담아줌
    for i in range(R):
        for j in range(C):
            if mini_map[i][j] > 0:
                dusts.append([i, j, mini_map[i][j]])

    # 담긴 먼지 리스트를 처리
    for dust in dusts:
        for k in range(4):
            nx = dust[0] + dx[k]
            ny = dust[1] + dy[k]
            if iswall(nx, ny) or mini_map[nx][ny] == -1:
                pass
            else:
                mini_map[nx][ny] += dust[2] // 5
                mini_map[dust[0]][dust[1]] -= dust[2] // 5


def up_iswall(i, j):
    if -1 < i < location[0][0] + 1 and -1 < j < C:
        return False
    return True


def down_iswall(i, j):
    if location[1][0] <= i < R and -1 < j < C:
        return False
    return True


def iswall(i, j):
    if -1 < i < R and -1 < j < C:
        return False
    return True


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

R, C, T = map(int, input().split())

mini_map = [list(map(int, input().split())) for _ in range(R)]


# 공기 청정기의 위치를 담아줌.
location = []
for i in range(R):
    for j in range(C):
        if mini_map[i][j] == -1:
            location.append([i, j])
time = 0
while time < T:
    time += 1
    # 확산을 시켜줌
    diffusion()
    # 위의 시뮬과 아래의 시뮬을 나눠서 계산
    up_simulation()
    down_simulation()

result = 0
for i in range(R):
    for j in range(C):
        result += mini_map[i][j]

print(result + 2)