import sys
sys.stdin = open('18231_ 파괴된_도시.txt')

def simulation(i):
    for j in range(len(citys[i])):
        if destroy[citys[i][j]] == 0:
            return
    tem.append(i + 1)
    result.append(i + 1)
    for j in range(len(citys[i])):
        result.append(citys[i][j] + 1)


N, M = map(int, input().split())

connects = [list(map(int, input().split())) for _ in range(M)]

K = int(input())
dummys = list(map(int, input().split()))
destroy = [0 for _ in range(N)]
tem = []
result = []
for dummy in dummys:
    destroy[dummy - 1] = 1
    if destroy == dummys:
        break


citys = [[] for _ in range(N)]

for connect in connects:
    citys[connect[0] - 1].append(connect[1] - 1)
    citys[connect[1] - 1].append(connect[0] - 1)

flag = 1
dummys = sorted(dummys)
for i in range(len(citys)):
    if destroy[i] == 1:
        simulation(i)
    result = set(result)
    result = list(result)
    result = sorted(result)


    if result == dummys:

        flag = 1
        break
    else:
        flag = 0
if flag:
    print(len(tem))
    print(' '.join(list(map(str, tem))))
else:
    print(-1)