import sys
sys.stdin = open('10282_해킹.txt')
import collections

def simulation(start):
    q = collections.deque([])
    q.append([start, 0])
    while len(q):
        here, sec = q.popleft()
        for i in range(n):
            if G[here][i] != 0 and dist[i] > sec + G[here][i]:
                q.append([i, sec + G[here][i]])
                dist[i] = sec + G[here][i]



T = int(input())
for tc in range(1, T + 1):
    n, d, c = map(int, input().split())
    G = [[0 for _ in range(n)] for _ in range(n)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        G[b - 1][a - 1] = s
    dist = [10000000 for _ in range(n)]
    cnt = 0
    dist[c - 1] = 0
    simulation(c - 1)
    sec = 0
    for i in range(len(dist)):
        if dist[i] != 10000000:
            cnt += 1
            if sec < dist[i]:
                sec = dist[i]
    print(cnt, sec)

