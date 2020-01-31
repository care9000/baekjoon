import sys
sys.stdin = open('11403_경로찾기.txt')

import collections

def bfs(i, j):
    q = collections.deque([j])
    while len(q):
        start = q.popleft()
        for k in range(N):
            if graph[start][k] and visited[i][k] == 0:
                visited[i][k] = 1
                q.append(k)




N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]


visited = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            bfs(i, j)
for i in range(len(visited)):
    for j in range(len(visited[i])):
        print(visited[i][j], end=' ')
    print()
