import sys
sys.stdin = open('6603_로또.txt')

def PowerSet(N, m, cnt):
    if cnt > 6:
        return
    if N == m:
        if cnt == 6:
            for i in range(len(A)):
                if A[i]:
                    print(lotto[i], end=" ")
            print()
        return
    else:
        A[m] = 1
        PowerSet(N, m + 1, cnt + 1)
        A[m] = 0
        PowerSet(N, m + 1, cnt)




while 1:
    dummy = list(map(int, input().split()))

    if dummy[0] == 0:
        break
    else:
        lotto = dummy[1:]

        A = [0] * dummy[0]

        PowerSet(dummy[0], 0, 0)
    print()