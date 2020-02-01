import sys
sys.stdin = open('1937_욕심쟁이_판다.txt')
import heapq

def ispass(i, j):
    if -1 < i < N and -1 < j < N:
        return True
    return False

N = int(input())

data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
mini_map = [[0 for _ in range(N)] for _ in range(N)]
orders = []
for i in range(N):
    for j in range(N):
        heapq.heappush(orders,[data[i][j], i, j])



dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while len(orders):
    order = heapq.heappop(orders)
    mini_map[order[1]][order[2]] = 1
    tem = 0
    for k in range(4):
        i_tem = order[1] + dx[k]
        j_tem = order[2] + dy[k]
        if ispass(i_tem, j_tem) and data[i_tem][j_tem] < data[order[1]][order[2]]:
            if mini_map[i_tem][j_tem] > tem:
                tem = mini_map[i_tem][j_tem]
    mini_map[order[1]][order[2]] += tem


result = 0
for i in range(N):
    for j in range(N):
        tem = mini_map[i][j]
        if tem > result:
            result = tem

print(result)