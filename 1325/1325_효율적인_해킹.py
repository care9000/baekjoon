import sys
sys.stdin = open('1325_효율적인_해킹.txt')
import collections
input = sys.stdin.readline

def bfs(start):
    q = collections.deque([])
    vis = [0 for _ in range(N + 1)]
    q.append(start)
    cnt = 0
    vis[start] = 1
    while len(q):
        here = q.popleft()
        for location in node[here]:
            if vis[location] == 0:
                cnt += 1
                vis[location] = 1
                q.append(location)

    return cnt


N, M = map(int, input().split())
node = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    node[B].append(A)


result = []
result_max = 0
for i in range(1, N + 1):
    if node[i]:
        tem_cnt = bfs(i)
        if tem_cnt > result_max:
            result_max = tem_cnt
            result = [i]

        elif tem_cnt == result_max:
            result.append(i)

for re in result:
    print(re, end=" ")
