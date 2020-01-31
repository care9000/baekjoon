import sys
sys.stdin = open('10026_적록색약.txt')

import collections

def bfs(i, j, cnt):
    q = collections.deque([])
    q.append([i, j])
    if cnt == 0:
        while len(q):
            location = q.popleft()
            i_location = location[0]
            j_location = location[1]
            for k in range(4):
                i_tem = i_location + i_move[k]
                j_tem = j_location + j_move[k]
                if ispass(i_tem, j_tem):
                    if area_map[i_tem][j_tem] == area_map[i_location][j_location]:
                        visited[i_tem][j_tem] = 1
                        q.append([i_tem, j_tem])
    else:
        while len(q):
            location = q.popleft()
            i_location = location[0]
            j_location = location[1]
            for k in range(4):
                i_tem = i_location + i_move[k]
                j_tem = j_location + j_move[k]
                if ispass(i_tem, j_tem):
                    if area_map[i_location][j_location] == 'R':
                        if area_map[i_tem][j_tem] != "B":
                            visited[i_tem][j_tem] = 1
                            q.append([i_tem, j_tem])
                    elif area_map[i_location][j_location] == 'G':
                        if area_map[i_tem][j_tem] != "B":
                            visited[i_tem][j_tem] = 1
                            q.append([i_tem, j_tem])
                    else:
                        if area_map[i_tem][j_tem] == "B":
                            visited[i_tem][j_tem] = 1
                            q.append([i_tem, j_tem])



def ispass(i, j):
    if -1 < i < N and -1 < j < N and visited[i][j] == 0:
        return True
    return False




i_move = [0, 0, -1, 1]
j_move = [-1, 1, 0, 0]



N = int(input())

area_map = [list(input()) for _ in range(N)]


for cnt in range(2):
    area = 0
    area_count = []
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            area += 1
            if visited[i][j] == 0:
                visited[i][j] = 1
                bfs(i, j, cnt)
    print(area)
    area_count.append(area)
print(area_count)