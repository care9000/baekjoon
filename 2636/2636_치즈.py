import sys
sys.stdin = open('치즈.txt')


import collections


def air_bfs(i, j):
    q = collections.deque([])
    q.append([i, j])
    while len(q):
        location = q.popleft()
        i_location = location[0]
        j_location = location[1]
        for move in range(4):
            i_tem = i_location + i_move[move]
            j_tem = j_location + j_move[move]
            if ispass(i_tem, j_tem) and air_visited[i_tem][j_tem] == 0 and my_map[i_tem][j_tem] == 0:
                air_visited[i_tem][j_tem] = 1
                q.append([i_tem, j_tem])




def bfs(i, j):
    q = collections.deque([])
    q.append([i, j])
    while len(q):
        location = q.popleft()
        i_location = location[0]
        j_location = location[1]
        for move in range(4):
            i_tem = i_location + i_move[move]
            j_tem = j_location + j_move[move]
            if ispass(i_tem, j_tem):
                if my_map[i_tem][j_tem] and visited[i_tem][j_tem] == 0:
                    visited[i_tem][j_tem] = 1
                    q.append([i_tem, j_tem])
                if air_visited[i_tem][j_tem] == 1 and [i_location, j_location] not in melt_list:
                    melt_list.append([i_location, j_location])


def ispass(i, j):
    if -1 < i < N and -1 < j < M :
        return True
    return False




# 4 방향 탐색
i_move = [0, 0, -1, 1]
j_move = [-1, 1, 0, 0]


N, M = map(int, input().split())
my_map = [list(map(int, input().split())) for _ in range(N)]

hour = 0

while 1:
    hour += 1
    visited = [[0 for _ in range(M)] for _ in range(N)]
    air = [[0 for _ in range(M)] for _ in range(N)]
    air_visited = [[0 for _ in range(M)] for _ in range(N)]
    air_visited[0][0] = 1
    air_bfs(0, 0)

    # 녹을 수 있는 치즈 위치를 list 하나에 담아둠
    melt_list = []
    flag = 0
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if my_map[i][j] and visited[i][j] == 0:
                flag = 1
                visited[i][j] = 1
                bfs(i, j)
    # 치즈 얼마나 남았나 계산 (이전)
    if flag == 0:
        break
    cheese = 0
    for i in range(N):
        for j in range(M):
            if my_map[i][j]:
                cheese += 1

    # 치즈 녹임
    for melt in melt_list:
        my_map[melt[0]][melt[1]] = 0
    # [print(my_map[i]) for i in range(N)]
    # print()


    # print("치즈", cheese)
print(hour - 1)
print(cheese)


