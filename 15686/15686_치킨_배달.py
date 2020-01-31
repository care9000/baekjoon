import sys
sys.stdin = open('15686_치킨_배달.txt')


def Distance():
    global min_distance

    distance = 0
    for i in range(len(house_location)):
        tem_distance = 987654321
        for j in range(len(chicken_location)):
            if A[j] == 1:
                if abs((house_location[i][0] - chicken_location[j][0])) + abs((house_location[i][1] - chicken_location[j][1])) < tem_distance:
                    tem_distance = abs((house_location[i][0] - chicken_location[j][0])) + abs((house_location[i][1] - chicken_location[j][1]))

        distance += tem_distance

    if min_distance > distance:
        min_distance = distance


def PowerSet(N, m):
    cnt = 0
    for i in range(len(A)):
        if A[i]:
            cnt += 1
    if cnt > M:
        return

    if N == m:
        cnt = 0
        for i in range(len(A)):
            if A[i]:
                cnt += 1
        if cnt == M:
            Distance()

    else:
        A[m] = 1
        PowerSet(N, m + 1)
        A[m] = 0
        PowerSet(N, m + 1)


N, M = map(int, input().split())

my_map = [list(map(int, input().split())) for _ in range(N)]

# 치킨 집, 집 위치 구하기
chicken_location = []
house_location = []
for i in range(N):
    for j in range(N):
        if my_map[i][j] == 2:
            chicken_location.append([i, j])
        elif my_map[i][j] == 1:
            house_location.append([i, j])

A = [0] * len(chicken_location)
min_distance = 987654321

PowerSet(len(chicken_location), 0)
print(min_distance)
