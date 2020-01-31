import sys
sys.stdin = open('1463_1로_만들기.txt')

N = int(input())

cnt = 0
while N != 1:
    if N % 3 == 0:
        cnt += 1
        N = N // 3

    if N % 2 == 0:
        cnt += 1
        N = N // 2
    cnt += 1
    N -= 1
    print(N)
print(cnt)