import sys
sys.stdin = open('1238_파티.txt')
import heapq
N, M, X = map(int, input().split())
distance_start = [[] for _ in range(N + 1)]
distance_end = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e, t = map(int, sys.stdin.readline().split())
    distance_start[e].append([s, t])
    distance_end[s].append([e, t])
dist_start = [100 * 10000 + 1 for _ in range(N + 1)]
dist_end = [100 * 10000 + 1 for _ in range(N + 1)]
dist_end[X] = 0
dist_start[X] = 0

q_start = []
heapq.heappush(q_start, [X, 0])
while len(q_start):
    end = heapq.heappop(q_start)

    for start in distance_start[end[0]]:
        if dist_start[start[0]] > dist_start[end[0]] + start[1]:
            dist_start[start[0]] = dist_start[end[0]] + start[1]
            heapq.heappush(q_start, [start[0], dist_start[start[0]]])

q_end = []
heapq.heappush(q_end, [X, 0])
while len(q_end):
    mid = heapq.heappop(q_end)
    for end in distance_end[mid[0]]:
        if dist_end[end[0]] > end[1] + dist_end[mid[0]]:
            dist_end[end[0]] = end[1] + dist_end[mid[0]]
            heapq.heappush(q_end, [end[0], dist_end[end[0]]])


result = 0
for i in range(1, N + 1):
    tem = dist_end[i] + dist_start[i]
    if result < tem:
        result = tem
print(result)
