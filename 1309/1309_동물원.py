import sys
sys.stdin = open('1309_동물원.txt')

N = int(input())

data_list = [3, 7]

for i in range(2, N):
    data_list.append(((data_list[i - 1] * 2) + data_list[i - 2]) % 9901)
print(data_list[N - 1] % 9901)

