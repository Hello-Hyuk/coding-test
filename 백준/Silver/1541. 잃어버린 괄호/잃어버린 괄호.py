import sys
input = sys.stdin.readline

# - 먼저 분리 모두 더한 후 다 빼기
tmp = str(input().strip())

tmp2 = tmp.split('-')
ans = []
for t in tmp2:
    if '+' in t:
        ans.append(sum(list(map(int, t.split('+')))))
    else :
        ans.append(int(t))
answer = 0
answer = ans[0]
if len(ans) == 1:  
    print(answer)
else :
    for i in ans[1:]:
        answer -= i
    print(answer)