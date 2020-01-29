import sys
sys.stdin = open('4963_섬의_개수.txt')

import collections

def bfs(i, j):
    visited[i][j] = 1
    q = collections.deque([])
    q.append([i, j])
    while len(q):
        location = q.popleft()
        i_location = location[0]
        j_location = location[1]
        for k in range(8):
            i_tem = i_location + dx[k]
            j_tem = j_location + dy[k]
            if ispass(i_tem, j_tem):
                visited[i_tem][j_tem] = 1
                q.append([i_tem, j_tem])

def ispass(i, j):
    if -1 < i < h and -1 < j < w and my_map[i][j] and visited[i][j] == 0:
        return True
    return False


# x = 가로, y = 세로 위, 아래, 좌, 우, 좌상, 우상, 좌하, 우하
dx = [0, 0, -1, 1, -1, 1, -1, 1]
dy = [-1, 1, 0, 0, -1, -1, 1, 1]


while 1:
    w, h = map(int, input().split())
    if w and h:
        my_map = [list(map(int, input().split())) for _ in range(h)]
        visited = [[0 for _ in range(w)] for _ in range(h)]
        island = 0
        for i in range(h):
            for j in range(w):
                if my_map[i][j] and visited[i][j] == 0:
                    island += 1
                    bfs(i, j)
        print(island)
    else:
        break