import sys
sys.stdin = open("안전 영역.txt")

import collections

# bfs 함수를 실행시켜 섬 크기 구하기
def bfs(i, j):
    global floor
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

# 갈 수 있는지 없는지 확인
def ispass(i, j):
    global floor
    if -1 < i < N and -1 < j < N and visited[i][j] == 0 and my_map[i][j] > floor:
        return True
    return False


# 네방향 확인 리스트
i_move = [0, 0, -1, 1]
j_move = [-1, 1, 0, 0]


N = int(input())

my_map = [list(map(int, input().split())) for _ in range(N)]

# 최대 높이를 뽑아냄 (height)
height = 0
for i in range(N):
    for j in range(N):
        if height < my_map[i][j]:
            height = my_map[i][j]

# 섬의 개수 구하기
island_max = 0
for floor in range(height):
    island = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # 방문하지 않고 홍수 높이보다 높을경우 bfs 실행
            if visited[i][j] == 0 and my_map[i][j] > floor:
                island += 1
                bfs(i, j)
    if island_max < island:
        island_max = island
print(island_max)