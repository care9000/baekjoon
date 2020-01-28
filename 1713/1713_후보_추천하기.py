import sys
sys.stdin = open('1713_후보_추천하기.txt')

def simulation(num):
    j = 0
    while 1:
        j += 1
        for k in range(len(Photo_Frame)):
            if Photo_Frame_recommendation[k] == j:
                Photo_Frame[k] = num
                Photo_Frame.append(Photo_Frame.pop(k))
                Photo_Frame_recommendation[k] = 1
                Photo_Frame_recommendation.append(Photo_Frame_recommendation.pop(k))
                return

N = int(input())
dummy = int(input())
recommendations = list(map(int, input().split()))

Photo_Frame = [0 for _ in range(N)]
Photo_Frame_recommendation = [0 for _ in range(N)]

for recommendation in recommendations:
    flag = 0

    # 만약 포토 프레임이 비어있으면 그자리에 추가
    for i in range(len(Photo_Frame)):
        if Photo_Frame[i] == 0:
            Photo_Frame[i] = recommendation
            Photo_Frame_recommendation[i] = 1
            flag = 1
            break
        elif Photo_Frame[i] == recommendation:
            Photo_Frame_recommendation[i] += 1
            flag = 1
            break

    if flag == 0:
        simulation(recommendation)

Photo_Frame = sorted(Photo_Frame)
for Photo in Photo_Frame:
    print(Photo, end=" ")