import sys
sys.stdin = open('2628_종이자르기.txt')
M, N = map(int, input().split())
Width_cut_list = []
Vertical_cut_list = []
T = int(input())
for _ in range(T):
    tem_a, tem_b = map(int, input().split())
    if tem_a:
        Vertical_cut_list.append(tem_b)
    else:
        Width_cut_list.append(tem_b)
# 정렬
Vertical_cut_list = sorted(Vertical_cut_list)
Width_cut_list = sorted(Width_cut_list)
Width_list = []
Vertical_list = []
cnt = 0
for i in range(M):
    if i in Vertical_cut_list:
        Vertical_list.append(cnt)
        cnt = 1
    else:
        cnt += 1

Vertical_list.append(cnt)

cnt = 0
for i in range(N):
    if i in Width_cut_list:
        Width_list.append(cnt)
        cnt = 1
    else:
        cnt += 1
Width_list.append(cnt)

result = 0
# 필요한 구역 별 길이를 저장후 데이터 들의 곱을 비교
for i in Width_list:
    for j in Vertical_list:
        if result < i * j:
            result = i * j
print(result)