import sys
sys.stdin = open('7569_토마토.txt')


import collections



def bfs(k, i, j):
    q = collections.deque([])
    q.append([i, j])
    location = q.popleft()
    i_location = location[0]
    j_location = location[1]
    for move in range(4):
        i_tem = i_location + i_move[move]
        j_tem = j_location + j_move[move]
        if ispass_1(k, i_tem, j_tem):
            visited[k][i_tem][j_tem] = 1
            next_ripe_list.append([k, i_tem, j_tem])
    if k == 0:
        if tomato_box[1][i][j] == 0 and visited[1][i][j] == 0:
            visited[1][i][j] = 1
            next_ripe_list.append([1, i, j])
    elif k == H - 1:
        if tomato_box[k - 1][i][j] == 0 and visited[k - 1][i][j] == 0:
            visited[k - 1][i][j] = 1
            next_ripe_list.append([k - 1, i, j])
    else:
        if tomato_box[k - 1][i][j] == 0 and visited[k - 1][i][j] == 0:
            visited[k - 1][i][j] = 1
            next_ripe_list.append([k - 1, i, j])
        if tomato_box[k + 1][i][j] == 0 and visited[k + 1][i][j] == 0:
            visited[k + 1][i][j] = 1
            next_ripe_list.append([k + 1, i, j])






def bfs_1(i, j):
    q = collections.deque([])
    q.append([i, j])


    location = q.popleft()
    i_location = location[0]
    j_location = location[1]
    for move in range(4):
        i_tem = i_location + i_move[move]
        j_tem = j_location + j_move[move]
        if ispass_1(0, i_tem, j_tem):
            visited[0][i_tem][j_tem] = 1
            next_ripe_list.append([0, i_tem, j_tem])


def bfs_2(k, i, j):
    q = collections.deque([])
    q.append([k, i, j])

    location = q.popleft()
    i_location = location[1]
    j_location = location[2]
    for move in range(4):
        i_tem = i_location + i_move[move]
        j_tem = j_location + j_move[move]
        if ispass_1(k, i_tem, j_tem):
            visited[k][i_tem][j_tem] = 1
            next_ripe_list.append([k, i_tem, j_tem])
    if k == 0:
        if tomato_box[1][i][j] == 0 and visited[1][i][j] == 0:
            visited[1][i][j] = 1
            next_ripe_list.append([1, i, j])
    else:
        if tomato_box[0][i][j] == 0 and visited[0][i][j] == 0:
            visited[0][i][j] = 1
            next_ripe_list.append([0, i, j])









def ispass_1(k, i, j):
    if -1 < i < N and -1 < j < M and tomato_box[k][i][j] == 0 and visited[k][i][j] == 0:
        return True
    return False

i_move = [0, 0, -1, 1, 0, 0]
j_move = [-1, 1, 0, 0, 0, 0]
h_move = [0, 0, 0, 0, -1, 0]

M, N, H = map(int, input().split())

tomato_box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0] * M for _ in range(N)] for _ in range(H)]

# 익은 토마토, 안익은 토마토, 토탈 토마토 갯수 구하기
ripe = 0
ripe_location_list = collections.deque([])
un_ripe = 0
total_tomato = 0
for k in range(H):
    for i in range(N):
        for j in range(M):
            if tomato_box[k][i][j] == 1:
                ripe_location_list.append([k, i, j])
                ripe += 1
                total_tomato += 1
            elif tomato_box[k][i][j] == 0:
                un_ripe += 1
                total_tomato += 1
# print(ripe_location_list)

# 익지 않은 토마토가 있을 경우 실행
day = 0
if un_ripe:
    while un_ripe:
        # [print(tomato_box[i]) for i in range(H)]
        # print()
        day += 1
        next_ripe_list = collections.deque([])
        next_ripe_tomato = 0
        # 익은 토마토 주변으로 확인
        while len(ripe_location_list):
            location = ripe_location_list.popleft()
            if H == 1:
                bfs_1(location[1], location[2])
            elif H == 2:
                bfs_2(location[0], location[1], location[2])
            else:
                bfs(location[0], location[1], location[2])

        # 익을 토마토 익히기
        while next_ripe_list:
            location = next_ripe_list.popleft()
            ripe_location_list.append([location[0], location[1], location[2]])
            tomato_box[location[0]][location[1]][location[2]] = 1
            next_ripe_tomato += 1
        un_ripe -= next_ripe_tomato

        if len(ripe_location_list) == 0:
            if un_ripe:
                day = - 1
                break
            else:
                break
elif ripe == 0:
    day = -1
print(day)