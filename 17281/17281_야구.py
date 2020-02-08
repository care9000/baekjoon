import sys
import itertools
sys.stdin = open('17281_야구.txt')


def simulation(batting):
    score = 0
    num = 0
    for inning in pre_score:
        out = 0
        b1, b2, b3 = 0, 0, 0
        while out < 3:
            if inning[batting[num]] == 0:
                out += 1
            elif inning[batting[num]] == 1:
                score += b3
                b3, b2, b1 = b2, b1, 1

            elif inning[batting[num]] == 2:
                score += b3 + b2
                b1, b2, b3 = 0, 1, b1

            elif inning[batting[num]] == 3:
                score += b3 + b2 + b1
                b1, b2, b3 = 0, 0, 1

            elif inning[batting[num]] == 4:
                score += 1 + b1 + b3 + b2
                b1, b2, b3 = 0, 0, 0

            num = (num + 1) % 9
    return score


N = int(input())
pre_score = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

maximum = N * 8 * 3
max_score = 0
ans = 0

for number in itertools.permutations(range(1, 9), 8):
    batting = list(number[:3]) + [0] + list(number[3:])
    ans = max(ans, simulation(batting))

print(ans)