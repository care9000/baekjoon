import sys
sys.stdin = open('14503_로봇_청소기.txt')

def simulation(i, j, dir):
    global work
    while 1:

        mission_1(i, j)
        #2번째 조건(세부조건 4개)
        if mission_2_a(i, j, dir):
            i = i + dx[(dir + 3) % 4]
            j = j + dy[(dir + 3) % 4]
            mini_map[i][j] = 2
            work += 1
            dir = (dir + 3) % 4
        elif mission_2_cd(i, j):
            if mission_2_c(i, j, dir):
                i = i + dx[(dir + 2) % 4]
                j = j + dy[(dir + 2) % 4]
            else:
                return
        else:
            dir = (dir + 3) % 4




def ispass(i, j):
    if -1 < i < N and -1 < j < M:
        if mini_map[i][j] == 0:
            return True
    return False




#1번째 조건인 청소
def mission_1(i, j):
    global work
    if mini_map[i][j] == 0:
        mini_map[i][j] = 2
        work += 1



#2-a조건
def mission_2_a(i, j, dir):
    i_tem = i + dx[(dir + 3) % 4]
    j_tem = j + dy[(dir + 3) % 4]
    # 왼쪽방향이 존재하고
    if ispass(i_tem, j_tem):
        return True
    return False

def mission_2_cd(i, j):
    for k in range(4):
        i_tem = i + dx[k]
        j_tem = j + dy[k]
        if ispass(i_tem, j_tem):
            return False
    return True

def mission_2_c(i, j, dir):
    i_tem = i + dx[(dir + 2) % 4]
    j_tem = j + dy[(dir + 2) % 4]
    if -1 < i_tem < N and -1 < j_tem < M and mini_map[i_tem][j_tem] == 2:
        return True
    return False
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
mini_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

work = 0
simulation(r, c, d)
print(work)