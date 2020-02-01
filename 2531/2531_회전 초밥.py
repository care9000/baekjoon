import sys
sys.stdin = open('2513_회전_초밥.txt')

N, d, k, c = map(int, sys.stdin.readline().split())
info = []
for i in range(N):
    info.append(int(sys.stdin.readline()))

for i in range(k):
    info.append(info[i])
max_result = []
i = 0
for i in range(N):
    data = info[i: i + k]
    data.append(c)
    tem = len(list(set(data)))

    max_result.append(tem)

print(max(max_result))
