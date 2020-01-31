import sys
sys.stdin = open('16234_인구_이동.txt')

import collections

def bfs(i, j):
    global cnt
    q = collections.deque([])
    q.append([i, j])
    visited[i][j] = 1
    data.append([i, j])
    while len(q):
        location = q.popleft()
        i_location = location[0]
        j_location = location[1]
        for move in range(4):
            i_tem = i_location + i_move[move]
            j_tem = j_location + j_move[move]
            if ispass(i_tem, j_tem) and L <= abs(country[i_location][j_location] - country[i_tem][j_tem]) <= R:
                visited[i_tem][j_tem] = 1
                data.append([i_tem, j_tem])
                q.append([i_tem, j_tem])

def ispass(i, j):
    if -1 < i < N and -1 < j < N and visited[i][j] == 0:
        return True
    return False


i_move = [0, 1, 0, -1]
j_move = [1, 0, -1, 0]

N, L, R = map(int, input().split())

country = [list(map(int, input().split())) for _ in range(N)]

day = 0


while day < 2001:
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            flag = 0
            if visited[i][j] == 0:
                cnt += 1
                data = []
                bfs(i, j)
                data_sum = 0
                for aaa in data:
                    data_sum += country[aaa[0]][aaa[1]]
                data_avg = data_sum // len(data)
                for aaa in data:
                    country[aaa[0]][aaa[1]] = data_avg

    if cnt == 0:
        break
    day += 1

    if 0 in visited:
        break
print(day)