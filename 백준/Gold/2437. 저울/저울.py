import sys
input = sys.stdin.readline

N = int(input())
stones = list(map(int,input().split()))
stones.sort()
# 구간을 정해서 넓혀가기
if stones[0] > 1:
    print(1)
else :
    answer = [0,stones[0]]
    for stone in stones[1:]:
        tmp = answer[0]+stone
        if answer[1]+1 < tmp:
            break
        else :
            answer = [0, answer[1]+stone]
    print(answer[1]+1)