import sys
sys.stdin = open('17136_색종이_붙이기.txt')


def dfs(i, j, cnt, dummy):
    global result

    if cnt > result:
        return

    elif dummy == 0:
        if cnt < result:
            result = cnt

    if ispass(i, j):
        if mini_map[i][j] == 1:
            for k in range(5, 0, -1):
                if papers[k] > 0 and ischeck(i, j, k):
                    change(i, j, k)
                    papers[k] -= 1
                    if j + k == 10:
                        dfs(i + 1, 0, cnt + 1, dummy - (k ** 2))
                    else:
                        dfs(i, j + k, cnt + 1, dummy - (k ** 2))
                    dechange(i, j, k)
                    papers[k] += 1
        else:
            if j + 1 == 10:
                dfs(i + 1, 0, cnt, dummy)
            else:
                dfs(i, j + 1, cnt, dummy)



def ischeck(i, j, k):

    for x in range(k):
        for y in range(k):
            if ispass(i + x, j + y) and mini_map[i + x][j + y] == 1:
                continue
            else:
                return False
    return True


def change(i, j, k):
    for x in range(k):
        for y in range(k):
            mini_map[i + x][j + y] = 0


def dechange(i, j, k):
    for x in range(k):
        for y in range(k):
            mini_map[i + x][j + y] = 1


def ispass(i, j):
    if -1 < i < 10 and -1 < j < 10:
        return True

    return False


papers = [0, 5, 5, 5, 5, 5]

mini_map = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]
dummy = 0
for i in range(10):
    for j in range(10):
        if mini_map[i][j] == 1:
            dummy += 1

result = 987654321
dfs(0, 0, 0, dummy)
if result == 987654321:
    print(-1)
else:
    print(result)