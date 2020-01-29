import sys
sys.stdin = open('빙산.txt')

import collections

def bfs(i, j):
    visited[i][j] = 1
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
                visited[i_tem][j_tem] = 1
                q.append([i_tem, j_tem])




# 갈 수 있는지 없는지 파악
def ispass(i, j):
    if -1 < i < N and -1 < j < M and visited[i][j] == 0 and my_map[i][j] != 0:
        return True
    return False





# 4방향 탐색
i_move = [0, 0, -1, 1]
j_move = [-1, 1, 0, 0]



N, M = map(int, input().split())
my_map = [list(map(int, input().split())) for _ in range(N)]

year = 0
flag = 0
#check
while 1:
    #섬 갯 수
    island = 0
    # 1 년 후
    year += 1
    destroy_list = []
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            cnt = 0
            # 빙산이 있을 때 만
            if my_map[i][j]:
                for move in range(4):
                    i_tem = i + i_move[move]
                    j_tem = j + j_move[move]
                    if my_map[i_tem][j_tem] == 0:
                        cnt += 1
                my_map[i][j] -= cnt
                # 바로 바꾸지 않고 나중에 끝나고 빙산을 녹임
                if my_map[i][j] < 1:
                    my_map[i][j] = 99
                    destroy_list.append([i, j])
    for destroy in destroy_list:
        my_map[destroy[0]][destroy[1]] = 0

    visited = [[0 for _ in range(M)] for _ in range(N)]
    # bfs 시작
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if visited[i][j] == 0 and my_map[i][j]:
                island += 1
                if island == 2:
                    flag = 1
                    break
                bfs(i, j)
        if flag == 1:
            break
    if flag == 1:
        break
    if island == 0:
        year = 0
        break
print(year)
