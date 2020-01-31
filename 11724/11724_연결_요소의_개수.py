import sys
sys.stdin = open('11724_연결_요소의_개수.txt')

import collections

def bfs(i):
    global Connected_Component
    q = collections.deque([i])

    while len(q):
        start = q.popleft()
        for k in range(N):
            if node[start][k] and visited[k] == 0:
                visited[k] = Connected_Component
                q.append(k)


N, M = map(int, input().split())
node_info_list = [list(map(int, input().split())) for _ in range(M)]

node = [[0 for _ in range(N)] for _ in range(N)]


# 노드를 그래프로 만듬
for node_info in node_info_list:
    node[node_info[0] - 1][node_info[1] - 1] = 1
    node[node_info[1] - 1][node_info[0] - 1] = 1

visited = [0] * N

# 연결 요소 구하기
Connected_Component = 0
for i in range(N):
    if visited[i] == 0:
        Connected_Component += 1
        visited[i] = Connected_Component
        bfs(i)

print(Connected_Component)
