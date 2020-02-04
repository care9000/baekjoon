import sys
sys.stdin = open('17281_야구.txt')
import itertools

def simulation(num, inning, score):
    global max_score

    if inning == N:
        if score > max_score:

            max_score = score
        return

    if max_score > score + (8 * 3) * (N - inning):

        return

    base = [0, 0, 0, 0, 0]
    out = 0
    while out < 3:
        num %= 9
        if pre_score[inning][positions[num]] == 0:
            out += 1

        else:
            move = pre_score[inning][positions[num]]
            if move == 4:
                score += 1

            for k in range(3, 0, -1):
                if base[k]:
                    if k + move >= 4:
                        score += 1
                        base[k] = 0
                    else:
                        base[k + move] = 1
                        base[k] = 0

            if move != 4:
                base[move] = 1
        num += 1
    simulation(num, inning + 1, score)






def Perm(n, m):
    global max_score, maximum
    if max_score == maximum:
        return

    if n == m:
        print(positions)
        simulation(0, 0, 0)
    elif m == 3:
        Perm(n, m + 1)

    else:
        for k in range(m, n):
            if k != 3:
                positions[m], positions[k] = positions[k], positions[m]
                Perm(n, m + 1)
                positions[m], positions[k] = positions[k], positions[m]

N = int(input())
pre_score = [list(map(int, input().split())) for _ in range(N)]
positions = [i for i in range(9)]
positions[0], positions[3] = positions[3], positions[0]
data = list(itertools.permutations(positions))
print(list(data))
maximum = N * 8 * 3
max_score = 0

# Perm(9, 0)
# print(max_score)