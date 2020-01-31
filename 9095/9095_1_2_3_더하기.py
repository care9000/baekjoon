import sys
sys.stdin = open('9095_1_2_3_더하기.txt')



T = int(input())
for tc in range(1, T + 1):
    data = [1, 2, 4]
    N = int(input())
    if N > 3:
        for i in range(N - 3):
            data.append(data[i] + data[i + 1] + data[i + 2])
        print(data[-1])
    else:
        print(data[N - 1])