import sys
sys.stdin = open('2583_영역_구하기.txt')

import collections

def bfs(i, j):
    global cnt
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
                cnt += 1
                q.append([i_tem, j_tem])

# 갈 수 있는지 없는지 확인

def ispass(i, j):
    if -1 < i < M and -1 < j < N and Graph_paper[i][j] == 0 and visited[i][j] == 0:
        return True
    return False


# 네방향 움직일 수 있는지 확인
i_move = [0, 0, -1, 1]
j_move = [-1, 1, 0, 0]
M, N, K = map(int, input().split())
# 직사각형의 정보를 받아옴
Square_info_list = [list(map(int, input().split())) for _ in range(K)]

# 모눈종이 맵을 만듬
Graph_paper = [[0] * N for _ in range(M)]

# 방문 리스트 만듬
visited = [[0] * N for _ in range(M)]

#직사각형의 정보들을 모눈종이에 표시
for Square_info in Square_info_list:
    for i in range(Square_info[1], Square_info[3]):
        for j in range(Square_info[0], Square_info[2]):
            Graph_paper[i][j] = 1

result = []
for i in range(len(Graph_paper)):
    for j in range(len(Graph_paper[i])):
        if Graph_paper[i][j] == 0 and visited[i][j] == 0:
            cnt = 1
            visited[i][j] = 1
            bfs(i, j)
            result.append(cnt)
result = sorted(result)
print(len(result))
for result_info in result:
    print(result_info, end=" ")
