import sys
sys.stdin = open('1547_공.txt')
M = int(input())
cup_location = [0, 1, 2, 3]
for _ in range(M):
    X, Y = map(int, input().split())
    i, j = 0, 0
    for k in range(1, 4):
        if X == cup_location[k]:
            i = k
        if Y == cup_location[k]:
            j = k
    cup_location[i], cup_location[j] = cup_location[j], cup_location[i]
print(cup_location[1])