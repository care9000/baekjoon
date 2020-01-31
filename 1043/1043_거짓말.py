import sys
sys.stdin = open('1043_거짓말.txt')



def party(i):
    global cnt
    for j in range(len(party_peoples[i])):
        if union(party_peoples[i][j]) == -1:
            return
    cnt += 1

def union(num):
    if relationship[num] == -1:
        return -1
    elif relationship[num] == num:
        return num
    else:
        return union(relationship[num])



def find_union(a, b):
    if union(a) < union(b):
        relationship[b] = union(a)
    else:
        relationship[a] = union(b)


N, M = map(int, input().split())

truth_peoples = list(map(int, input().split()))[1:]
party_peoples = [list(map(int, input().split()))[1:] for _ in range(M)]


relationship = [i for i in range(N + 1)]
# 진실을 알고 있는 사람은 -1 로 바까줌
for truth in truth_peoples:
    relationship[truth] = -1

# 파티에 참석한 사람들은 서로 관계가 있으므로 작은 넘버의 수로 표시
for _ in range(M):
    for i in range(M):
        for j in range(len(party_peoples[i]) - 1):
            for k in range(j + 1, len(party_peoples[i])):
                find_union(party_peoples[i][j], party_peoples[i][k])

#과장을 할 수 있는 파티에서는 과장(cnt)하기
cnt = 0
for i in range(M):
    party(i)
print(cnt)