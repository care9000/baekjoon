import sys
sys.stdin = open('13913_숨바꼭질.txt')
import collections

def find_simulation():
    q = collections.deque([])
    vis[N] = 0
    q.append(N)
    while len(q):
        location = q.popleft()
        if location == K:
            print(vis[location])
            return
        if is_method_1(location):
            vis[location - 1] = vis[location] + 1
            if location - 1 == K:
                print(vis[location] + 1)
                return
            q.append(location - 1)

        if is_method_2(location):
            vis[location + 1] = vis[location] + 1
            if location + 1 == K:
                print(vis[location] + 1)
                return
            q.append(location + 1)

        if is_method_3(location):
            vis[location * 2] = vis[location] + 1
            if location * 2 == K:
                print(vis[location] + 1)
                return
            q.append(location * 2)
    return


def is_method_1(i):
    if 0 < i and vis[i - 1] > vis[i] + 1:
        return True
    return False


def is_method_2(i):
    if i + 1 < K + 1 and vis[i + 1] > vis[i] + 1:
        return True
    return False


def is_method_3(i):
    if i * 2 < K + 2 and vis[i * 2] > vis[i] + 1:
        return True
    return False


N, K = map(int, input().split())

max_num = max(N, K)
# 최대보다 하나 더찍어서 계산해야함
vis = [987654321 for _ in range((max_num * 2) + 2)]

find_simulation()

start = K
route = collections.deque([])
route.append(start)
while 1:
    start = route[0]
    for k in range(3):
        if k == 0:
            if 0 < start and vis[start - 1] == vis[start] - 1:
                route.appendleft(start - 1)
                break

        elif k == 1:
            if vis[start + 1] == vis[start] - 1:
                route.appendleft(start + 1)
                break

        else:
            if start % 2 == 0 and vis[start // 2] == vis[start] - 1:
                route.appendleft(start // 2)
                break
    if start == route[0]:
        break
if N == K:
    print(K)
else:
    for result in route:
        print(result, end=" ")

