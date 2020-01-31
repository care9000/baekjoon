import sys
sys.stdin = open('1003_피보나치_함수.txt')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    fibo = [[1, 0], [0, 1], [1, 1]]
    for i in range(N - 1):
        fibo.append([fibo[-1][0] + fibo[-2][0], fibo[-1][1] + fibo[-2][1]])
    if N == 0:
        print(fibo[0][0], end = " ")
        print(fibo[0][1])
    elif N == 1:
        print(fibo[1][0], end=" ")
        print(fibo[1][1])
    else:
        print(fibo[-2][0], end=" ")
        print(fibo[-2][1])
