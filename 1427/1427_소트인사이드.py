import sys
sys.stdin = open('1427_소트인사이드.txt')

input_data = input()
data = []
for put in input_data:
    data.append(int(put))
data = sorted(data, reverse=True)
for i in data:
    print(i, end="")


