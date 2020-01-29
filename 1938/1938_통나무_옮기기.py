import sys
sys.stdin = open('1938_통나무_옮기기.txt')

import collections
def bfs(i, j, type):
    global result
    q.append([i, j, type, 0])
    while len(q):
        # print(q)
        i, j, type, cnt = q.popleft()
        # 그 지점이 끝점과 같으면 결과 출력하고 리턴
        if i == finish[0] and j == finish[1] and type == finish[2]:
            result = cnt
            return
        tem = 0

        for x in range(-1, 2, 1):
            for y in range(-1, 2, 1):
                if ispass(i + x, j + y):
                    tem += 1

        #회전 가능하면
        if tem == 9:
            if type == 0:
                if visited_vertical[i][j] == 0:
                    visited_vertical[i][j] = cnt + 1
                    q.append([i, j, 1, cnt + 1])
            else:
                if visited_horizontal[i][j] == 0:
                    visited_horizontal[i][j] = cnt + 1
                    q.append([i, j, 0, cnt + 1])

        for k in range(4):
            i_tem = i + dx[k]
            j_tem = j + dy[k]
            if type == 0:
                if type_0(i_tem, j_tem) and visited_horizontal[i_tem][j_tem] == 0:
                    visited_horizontal[i_tem][j_tem] = cnt + 1
                    q.append([i_tem, j_tem, type, cnt + 1])
            else:
                if type_1(i_tem, j_tem) and visited_vertical[i_tem][j_tem] == 0:
                    visited_vertical[i_tem][j_tem] = cnt + 1
                    q.append([i_tem, j_tem, type, cnt + 1])


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def ispass(i, j):
    if -1 < i < N and -1 < j < N and mini_map[i][j] == 0:
        return True
    return False


def type_0(i_tem, j_tem):
    for j in range(-1, 2, 1):
        if -1 < i_tem < N and -1 < j_tem + j < N and mini_map[i_tem][j_tem + j] == 0:
            continue
        else:
            return False
    return True


def type_1(i_tem, j_tem):
    for i in range(-1, 2, 1):
        if -1 < i_tem + i < N and -1 < j_tem < N and mini_map[i_tem + i][j_tem] == 0:
            continue
        else:
            return False
    return True
N = int(input())
dummy = [input() for _ in range(N)]

mini_map = [[0 for _ in range(N)] for _ in range(N)]

# 가로 세로 visited 를 따로 만들어줌
visited_horizontal = [[0 for _ in range(N)] for _ in range(N)]
visited_vertical = [[0 for _ in range(N)] for _ in range(N)]

start_list = []
finish_list = []
for i in range(N):
    for j in range(N):
        if dummy[i][j] == '1':
            mini_map[i][j] = 1
        elif dummy[i][j] == 'B':
            start_list.append([i, j])
        elif dummy[i][j] == 'E':
            finish_list.append([i, j])

#가로는 0, 세로는 1 을 하고 중간점을 시작점으로 담아줌
if start_list[0][0] - start_list[1][0] == 0:
    start = [start_list[1][0], start_list[1][1], 0]
else:
    start = [start_list[1][0], start_list[1][1], 1]

# 끝점도 마찬 가지로 담아줌
if finish_list[0][0] - finish_list[1][0] == 0:
    finish = [finish_list[1][0], finish_list[1][1], 0]
else:
    finish = [finish_list[1][0], finish_list[1][1], 1]
result = 0

q = collections.deque([])
bfs(start[0], start[1], start[2])
print(result)
# [print(visited_horizontal[i]) for i in range(N)]
# print()
# [print(visited_vertical[i]) for i in range(N)]