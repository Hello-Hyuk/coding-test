import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
# 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)
operator = list(map(int, sys.stdin.readline().split()))

max_, min_ = 0, 0
def dfs(cnt, num, op):
    global max_, min_
    if cnt == n - 1:
        max_ = max(num, max_)
        min_ = min(num, min_)
    
    else:
        if op[0] > 0:
            dfs(cnt + 1, num + nums[cnt+1], [op[0]-1, op[1], op[2], op[3]])
        if op[1] > 0:
            dfs(cnt + 1, num - nums[cnt+1], [op[0], op[1]-1, op[2], op[3]])
        if op[2] > 0:
            dfs(cnt + 1, num * nums[cnt+1], [op[0], op[1], op[2]-1, op[3]])
        if op[3] > 0:
            dfs(cnt + 1, int(num / nums[cnt+1]), [op[0], op[1], op[2], op[3]-1])

dfs(0, nums[0], operator)

print(min(max_,100000000))
print(max(min_,-100000000))