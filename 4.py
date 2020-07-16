import collections

def bfs(i):
    q = collections.deque([])
    q.append([info[i][1], int(info[i][2])])
    while len(q):
        tem = q.popleft()
        shape, cost = tem[0], tem[1]
        for j in range(len(info)):
            if shape == info[j][0] and vis[j] > int(info[j][2]) + cost:
                vis[j] = int(info[j][2]) + cost
                q.append([info[j][1], int(info[j][2]) + cost])
                if info[j][1] == end:
                    return int(info[j][2]) + cost
    return -1





N, M = map(int, input().split())
info = [list(input().split()) for _ in range(M)]
q = int(input())
data = [list(input().split()) for _ in range(q)]
for a in range(len(data)):
    start, end = data[a][0], data[a][1]
    result = 10000000
    if start == end:
        result = 0
    else:
        for i in range(len(info)):
            if info[i][0] == start:
                vis = [10000000 for _ in range(M)]
                vis[i] = int(info[i][2])
                if info[i][1] == end:
                    tem = int(info[i][2])
                else:
                    tem = bfs(i)
                if tem < result and tem != -1:
                    result = tem
        if result == 10000000:
            result = -1
    print(result)

