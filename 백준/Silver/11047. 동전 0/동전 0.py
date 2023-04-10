import sys
input = sys.stdin.readline

N, K = map(int,input().split())
answer = 0
moneys = []
for _ in range(N):
    money = int(input())
    if money <= K:
        moneys.append(money)
moneys.sort(reverse=True)

for money in moneys:
    times, left = divmod(K,money)
    K = left
    answer += times
    if left == 0:
        break
print(answer)