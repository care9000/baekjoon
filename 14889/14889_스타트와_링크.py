import sys
sys.stdin = open('14889_스타트와_링크.txt')


def attend():
    global diffrence
    start = []
    link = []
    start_Stats = 0
    link_Stats = 0
    for i in range(N):
        if player[i]:
            start.append(i)
        else:
            link.append(i)

    for i in range((N // 2) - 1):
        for j in range(i + 1, (N // 2)):
            start_Stats += soccer[start[i]][start[j]]
            start_Stats += soccer[start[j]][start[i]]
            link_Stats += soccer[link[i]][link[j]]
            link_Stats += soccer[link[j]][link[i]]
    if abs(start_Stats - link_Stats) < diffrence:
        diffrence = abs(start_Stats - link_Stats)




def PowerSet(N, m):
    if diffrence == 0:
        return
    cnt = 0
    for i in range(N):
        if player[i]:
            cnt += 1
    if cnt > N // 2:
        return
    if N == m:
        cnt = 0

        for i in range(N):
            if player[i]:
                cnt += 1
        if cnt == N // 2:
            attend()
    else:
        player[m] = 1
        PowerSet(N, m + 1)
        player[m] = 0
        PowerSet(N, m + 1)


N = int(input())

soccer = [list(map(int, input().split())) for _ in range(N)]


player = [0] * N

diffrence = 987654321

PowerSet(N, 0)
print(diffrence)