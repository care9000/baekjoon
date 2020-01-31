import sys
sys.stdin = open('단지번호붙이기.txt')

import collections

# 아파트 내의 확인
def bfs(i, j):
    global Apartment_complex
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
                visited[i_tem][j_tem] = Apartment_complex
                q.append([i_tem, j_tem])


# 이동 가능한지 안한지 확인
def ispass(i, j):
    if -1 < i < N and -1 < j < N and my_map[i][j] and visited[i][j] == 0:
        return True
    return False



# 4 방향 탐색
i_move = [0, 0, -1, 1]
j_move = [-1, 1, 0, 0]


N = int(input())
my_map = [[int(i) for i in input()] for j in range(N)]


# 방문 여부를 위해 visited_list만듬
visited = [[0 for _ in range(N)] for _ in range(N)]
Apartment_complex = 0
for i in range(N):
    for j in range(N):
        if my_map[i][j] and visited[i][j] == 0:
            Apartment_complex += 1
            visited[i][j] = Apartment_complex
            bfs(i, j)
Apartment_complex_list =[0] * (Apartment_complex + 1)
for i in range(N):
    for j in range(N):
        Apartment_complex_list[visited[i][j]] += 1
print(Apartment_complex)
Apartment_complex_list = sorted(Apartment_complex_list[1:])
for i in range(0, len(Apartment_complex_list)):
    print(Apartment_complex_list[i])




