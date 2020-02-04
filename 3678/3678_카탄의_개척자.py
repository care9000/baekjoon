import sys
sys.stdin = open('3678_카탄의_개척자.txt')

def simulation(num):
    tem = []
    for adj in adjacency:
        tem.append(data[adj])
    tem.append(data[num - 1])

    min_num = 987654321
    min_location = 0
    for j in range(1, 6):
        if j not in tem:
            if min_num > uses[j]:
                min_num = uses[j]
                min_location = j
    data.append(min_location)
    uses[min_location] += 1
    if len(adjacency) == 1:
        adjacency.append(adjacency[0] + 1)
    else:
        adjacency.pop(0)






N = int(input())
info = list(int(input()) for _ in range(N))
data = [0, 1, 2, 3, 4, 5, 2, 3, 1, 4]
uses = [0, 2, 2, 2, 2, 1]
max_num = max(info)
adjacency = [2, 3]
for i in range(10, max_num + 1):
    simulation(i)

for i in info:
    print(data[i])

