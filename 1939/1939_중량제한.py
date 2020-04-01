import sys
sys.stdin = open('1939_중량제한.txt')
input = sys.stdin.readline
import collections

def bfs(start):
    q = collections.deque([])
    vis = [0 for _ in range(N + 1)]
    vis[start] = 1000000000
    q.append([start, 1000000000])
    while len(q):
        data = q.popleft()
        here, weight = data[0], data[1]
        for now in G[here]:
            tem, tem_weight = now[0], now[1]
            if weight < tem_weight:
                tem_weight = weight

            if vis[tem] < tem_weight:
                vis[tem] = tem_weight
                q.append([tem, tem_weight])

    return vis[finish]


N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    G[A].append([B, C])
    G[B].append([A, C])

start, finish = map(int, input().split())
print(bfs(start))