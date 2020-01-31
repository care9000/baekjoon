import sys
sys.stdin = open('2960_에라토스테네스의_체.txt')

def Sieve_of_Eratosthenes():
    global cnt
    while cnt < K:
        # 2 부터 시작
        for i in range(2, len(data)):
            tem = data[i]
            # data[i] 의 수가 지워지지 않으면 들어감
            if tem:
                # data[i] 의 배수가 0 이 아닐 시에는 0으로 만들고 cnt 하나 증가 시켜줌
                for j in range(1, (N // tem) + 1):
                    result = i * j
                    if data[result]:
                        data[i * j] = 0

                        cnt += 1
                        if cnt == K:
                            print(result)
                            return

N, K = map(int, input().split())

# 0 ~ N 까지 리스트 만들어줌
data = [i for i in range(N + 1)]
cnt = 0
Sieve_of_Eratosthenes()




