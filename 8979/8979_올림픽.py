import sys
sys.stdin = open('8979_올림픽.txt')
#순위 정하기
def dubble_sorted(a):
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[i][1] < a[j][1]:
                a[i], a[j] = a[j], a[i]
            elif a[i][1] == a[j][1]:
                if a[i][2] < a[j][2]:
                    a[i], a[j] = a[j], a[i]
                elif a[i][2] == a[j][2]:
                    if a[i][3] < a[j][3]:
                        a[i], a[j] = a[j], a[i]

N, K = map(int, input().split())
nation = [list(map(int, input().split())) for _ in range(N)]
dubble_sorted(nation)

rank = 1
rank_list = [0 for _ in range(N)]
# 랭킹 순위를 리스트로 만듬
tem = 0
for i in range(N - 1):
    rank_list[i] = rank
    if nation[i][1:] != nation[i + 1][1:]:
        rank += 1
        rank += tem
        tem = 0
    else:
        tem += 1
rank_list[-1] = rank


for i in range(N):
    if nation[i][0] == K:
        print(rank_list[i])


