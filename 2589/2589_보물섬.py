import sys
sys.stdin = open('2589_보물섬.txt')

import collections

def bfs(i, j):

    q = collections.deque([])
    q.append([i, j])

    while len(q):
        location = q.popleft()
        i_location = location[0]
        j_location = location[1]
        # 4방향 탐색
        for move in range(4):
            i_tem = i_location + i_move[move]
            j_tem = j_location + j_move[move]
            if ispass(i_tem, j_tem):
                visited[i_tem][j_tem] = visited[i_location][j_location] + 1
                q.append([i_tem, j_tem])

def ispass(i, j):
    if -1 < i < N and -1 < j < M and Treasure_map[i][j] == 'L' and visited[i][j] == 0:
        return True
    return False



i_move = [0, 0, -1 ,1]
j_move = [-1, 1, 0, 0]




N, M = map(int, input().split())


Treasure_map = [list(input()) for _ in range(N)]

distance = -1

for i in range(N):
    for j in range(M):
        if Treasure_map[i][j] == 'L':
            visited = [[0 for _ in range(M)] for _ in range(N)]
            visited[i][j] = 1
            bfs(i, j)
            tem = 0
            for ii in range(N):
                for jj in range(M):
                    if visited[ii][jj] > tem:
                        tem = visited[ii][jj]

            if distance < tem and tem != 1:
                distance = tem
print(distance - 1)
