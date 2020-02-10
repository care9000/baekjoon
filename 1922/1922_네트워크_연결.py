import sys
sys.stdin = open('1922_네트워크_연결.txt')


def kruskal():
    mst = []
    mst_value = 0
    i = 0
    while len(mst) < N - 1:
        a, b, value = connections[i]
        if find_set(a) != find_set(b):
            Union(a, b)
            mst_value += value
            mst.append([a, b])
        i += 1
    return mst_value


def find_set(a):
    if a == PI[a]:
        return a
    else:
        return find_set(PI[a])


def Union(a, b):
    if a < b:
        PI[find_set(b)] = find_set(a)

    else:
        PI[find_set(a)] = find_set(b)

N = int(input())
M = int(input())
connections = [list(map(int, input().split())) for  _ in range(M)]
connections.sort(key=lambda x: x[2])

PI = [i for i in range(N + 1)]

result = kruskal()
print(result)