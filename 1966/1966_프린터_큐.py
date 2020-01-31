import sys
sys.stdin = open('1966_프린터_큐.txt')

import collections


def bubble_sorted(a):
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[i][1] < a[j][1]:
                a[i], a[j] = a[j], a[i]



T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    importance_list = list(map(int, input().split()))

    data = collections.deque([])

    for i in range(N):
        data.append([i, importance_list[i]])

    i = 0
    while 1:
        flag = 0
        for j in range(1, len(data)):
            if data[0][1] < data[j][1]:
                flag = 1
                break
        if flag == 0:
            i += 1
            tem = data.popleft()
            if tem[0] == M:
                break
        else:
            data.append(data.popleft())

    print(i)