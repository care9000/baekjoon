import sys
sys.stdin = open('5179_거의_최단_경로.txt')
input = sys.stdin.readline
import collections


def Dijkstra(start):
    q = collections.deque([])
    for j in range(N):
        if adj[start][j]:
            dist[j] = adj[start][j]
            q.append(j)
    while len(q):
        i = q.popleft()
        for j in range(N):
            if adj[i][j] and dist[i] + adj[i][j] < dist[j]:
                dist[j] = dist[i] + adj[i][j]
                q.append(j)


def find_Dijkstra(end):
    q = collections.deque([])
    q.append(end)
    while len(q):
        i = q.popleft()
        for j in range(N):
            if adj[j][i] and adj[j][i] + dist[j] == dist[i]:
                adj[j][i] = 0
                q.append(j)

while 1:
    N, M = map(int, input().split())
    if N == 0:
        break

    S, D = map(int, input().split())
    dummys = [list(map(int, input().split())) for _ in range(M)]
    adj = [[0 for _ in range(N)] for _ in range(N)]
    for dummy in dummys:
        adj[dummy[0]][dummy[1]] = dummy[2]
    dist = [987654321 for _ in range(N)]
    dist[S] = 0
    Dijkstra(S)
    if dist[D] == 987654321:
        print(-1)
    else:
        find_Dijkstra(D)
        dist = [987654321 for _ in range(N)]
        Dijkstra(S)
        if dist[D] == 987654321:
            print(-1)
        else:
            print(dist[D])