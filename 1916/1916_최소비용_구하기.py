import sys
import collections
sys.stdin = open('1916_최소비용_구하기.txt')
input = sys.stdin.readline


def simulation():
    q = collections.deque([])
    q.append(start)
    while len(q):
        here = q.popleft()
        for tem in graph[here]:
            city, cost = tem[0], tem[1]
            # 현재까지 도시의 비용과 city 까지의 합한 비용이 (dis[city]) 보다 더 작으면 갱신
            if distance[here] + cost < distance[city]:
                q.append(city)
                distance[city] = distance[here] + cost


N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, cost = map(int, input().split())
    graph[A].append([B, cost])
start, end = map(int, input().split())
distance = [100000 * N] * (N + 1)
distance[start] = 0
simulation()
print(distance[end])