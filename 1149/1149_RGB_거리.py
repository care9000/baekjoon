import sys
sys.stdin = open('1149_RGB_거리.txt')

house_cnt = int(input())
house_cost = [list(map(int, input().split())) for _ in range(house_cnt)]
for i in range(1, house_cnt):
    for j in range(3):
        tem = 987654321
        for k in range(3):
            if j != k:
                if house_cost[i - 1][k] < tem:
                    tem = house_cost[i - 1][k]
        house_cost[i][j] += tem
print(min(house_cost[-1]))