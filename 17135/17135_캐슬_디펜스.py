import sys
sys.stdin = open('17135_캐슬_디펜스.txt')


def simulation():
    global hunt
    archer_location = []
    for i in range(len(Archer)):
        if Archer[i]:
            archer_location.append([N, i])

    monster = len(monster_location)
    temp_monster_location = []
    for m in monster_location:
        temp_monster_location.append([m[0], m[1]])
    hunt_temp = 0
    # print(monster)
    while monster:
        # print(temp_monster_location)
        hunt_monster = []
        for archer in archer_location:
            length = 987654321
            for idx, temp in enumerate(temp_monster_location):
                #사냥 시작
                if temp[0] < N:
                    if abs(archer[0] - temp[0]) + abs(archer[1] - temp[1]) < D + 1:
                        if abs(archer[0] - temp[0]) + abs(archer[1] - temp[1]) < length:
                            aa = idx
                            length = abs(archer[0] - temp[0]) + abs(archer[1] - temp[1])
                        elif length == abs(archer[0] - temp[0]) + abs(archer[1] - temp[1]):
                            if temp_monster_location[aa][1] > temp[1]:
                                aa = idx

            if length != 987654321:
                if aa not in hunt_monster:
                    hunt_monster.append(aa)
        # print(hunt_monster)
        for hunt_mon in hunt_monster:
            temp_monster_location[hunt_mon][0] = N
            hunt_temp += 1
            monster -= 1




        # print(hunt_temp)
        for temp in temp_monster_location:
            if temp[0] != N:
                temp[0] += 1
                if temp[0] == N:
                    monster -= 1
            # print(monster)

    if hunt < hunt_temp:
        hunt = hunt_temp






def Power_set(M, m, cnt):
    if cnt > 3:
        return

    elif M == m:
        if cnt == 3:
            simulation()

    else:
        Archer[m] = 1
        Power_set(M, m + 1, cnt + 1)
        Archer[m] = 0
        Power_set(M, m + 1, cnt)


N, M, D = map(int, input().split())

my_map = [list(map(int,input().split())) for _ in range(N)]

monster_location = []

for i in range(N - 1, -1, -1):
    for j in range(M):
        if my_map[i][j]:
            monster_location.append([i, j])

# print(monster_location)
Archer = [0] * M
hunt = 0
Power_set(M, 0, 0)
print(hunt)