import sys
sys.stdin = open('15686_치킨_배달.txt')


def simulation():
    global mini_mum_distance

    #집과 치킨집간의 거리구하기
    tem_mini_mum_distance = 0
    for home in house:
        tem = 987654321
        for i in range(len(chicken_house)):
            if A[i] == 1:
                distance = abs(home[0] - chicken_house[i][0]) + abs(home[1] - chicken_house[i][1])
                if tem > distance:
                    tem = distance
        tem_mini_mum_distance += tem
        if tem_mini_mum_distance > mini_mum_distance:
            return

    if tem_mini_mum_distance < mini_mum_distance:
        mini_mum_distance = tem_mini_mum_distance


def PowerSet(n, m, cnt):
    if cnt == M:
        simulation()

    elif n == m:
        return

    else:
        A[m] = 1
        PowerSet(n, m + 1, cnt + 1)
        A[m] = 0
        PowerSet(n, m + 1, cnt)



N, M = map(int, input().split())
mini_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

house = []
chicken_house = []
for i in range(N):
    for j in range(N):
        if mini_map[i][j] == 1:
            house.append([i, j])

        elif mini_map[i][j] == 2:
            chicken_house.append([i, j])


A = [0 for _ in range(len(chicken_house))]
mini_mum_distance = 987654321
PowerSet(len(chicken_house), 0, 0)
print(mini_mum_distance)