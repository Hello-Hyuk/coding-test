import sys
input = sys.stdin.readline

A = int(input())
num_list = list(map(int,input().split()))
answer = []
tmp_list = []
for i in range(A-1,-1,-1):
    while tmp_list and tmp_list[-1] <= num_list[i]:
        tmp_list.pop()
    
    answer.append(tmp_list[-1] if tmp_list else -1)
    tmp_list.append(num_list[i])    
print(*answer[::-1])