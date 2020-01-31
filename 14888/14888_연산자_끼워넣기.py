import sys
sys.stdin = open('14888_연산자_끼워넣기.txt')

def dfs(num, result):
    global max_sum, min_sum
    # 결과 값이 - 10억 부터 10억 까지이다.
    if num == N:
        if max_sum < result and - 1000000000 <= result <= 1000000000:
            max_sum = result
        if min_sum > result and - 1000000000 <= result <= 1000000000:
            min_sum = result
        return

    else:
        for i in range(4):
            # 덧셈
            if i == 0 and operator[i]:
                operator[i] -= 1
                dfs(num + 1, result + A[num])
                operator[i] += 1

            # 뺄셈
            elif i == 1 and operator[i]:
                operator[i] -= 1
                dfs(num + 1, result - A[num])
                operator[i] += 1

            # 곱셈
            elif i == 2 and operator[i]:
                operator[i] -= 1
                dfs(num + 1, result * A[num])
                operator[i] += 1

            # 나눗셈
            elif i == 3 and operator[i]:
                operator[i] -= 1
                if result < 0:
                    dfs(num + 1, -((- result) // A[num]))
                else:
                    dfs(num + 1, result // A[num])
                operator[i] += 1

N = int(input())

A = list(map(int, input().split()))
operator = list(map(int, input().split()))


# 최댓값 최솟값 초기화
max_sum = -1000000000
min_sum = 1000000000
dfs(1, A[0])
print(max_sum)
print(min_sum)
