import sys
sys.stdin = open('1912_연속합.txt')

n = int(input())
num_list = list(map(int, input().split()))

result = 0
tem = 0
if max(num_list) < 0:
    print(max(num_list))

else:
    for num in num_list:
        # 일단 숫자가 0 보다 크면 더해주기
        if num > 0:
            tem += num
        else:
            # 0보다 작을 경우 경우의수 생각

            if tem > result:
                result = tem
            # 이제 계산값이 0보다 클경우는 더해주고 아닐경우에는 그다음 부터 다시 시작
            tem += num
            if tem < 0:
                tem = 0

    if tem > result:
        result = tem
    print(result)


