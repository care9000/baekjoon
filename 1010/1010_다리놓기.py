import sys
sys.stdin = open('1010_다리놓기.txt')

def PowerSet(M, m, cnt):
    global number_of_cases
    if cnt > N:
        return
    elif cnt == N:
        number_of_cases += 1
        return
    elif M == m:
        return
    else:
        PowerSet(M, m + 1, cnt + 1)
        PowerSet(M, m + 1, cnt)



T = int(input())
for tc in range(1 ,T + 1):
    N, M = map(int, input().split())
    number_of_cases = 0
    if M - N < N:
        N = M - N
    # # 1번째 M 개중에서 2번째 애를 선택할 건지 말건지 그리고 선택했다면 cnt ++ 해줄것
    # PowerSet(M, 0, 0)
    # print(number_of_cases)
    result = 1
    for i in range(M - N):
        result *= (M - i)
        i += 1

    i = 0
    for j in range(M - N):
        result //= ((M - N) - j)
    print(result)