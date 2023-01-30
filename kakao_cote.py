#1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
def solution(x, y, z):
    # Write your code here
    # 차이와 z의 관계 
    # 차이 > z
    diff = abs(x-y)
    if diff > z:
        return -1
    # 차이 == z
    elif diff == z:
        return max(x,y)
    elif diff < z :
        # x, y 동일 시
        if x==y:
            # 홀수 일때 불가능
            if z % 2 == 1:
                return -1
            # 짝수일 때
            elif z%2== 0 :
                return x+(z//2)
        elif x>y:
            # x y 간격이 홀수 이고 z가 짝수
            if diff%2 == 1:
                if z%2 == 0:
                    return -1
                elif z%2==1:
                    return x + (z-diff)//2
            elif diff%2 == 0:
                if z%2 == 0:
                    return x + (z-diff)//2
                elif z%2==1 :
                    return -1
        # if   4  6  6    5-8 이상 홀수 가능 짝수 불가능
        # 1 2 3 4 5 6 7 8 9 10
        elif x<y:
            if diff%2 == 1:
                if z%2 == 0:
                    return -1
                elif z%2==1:
                    return y + (z-diff)//2
            elif diff%2==0:
                if z%2 == 0:
                    return y + (z-diff)//2
                elif z%2==1:
                    return -1






# 1 2 3 4 5 6 7 8 9 10 11 12 13
# 8 4 5 

### prob 2 n = len(cost)
n, cost = map(int, input().split())
## num find
num = []
thing = [[0,0]]
d = [[0]*(cost+1) for _ in range(n+1)]

for i in range(n):
    thing.append([cost[i],num[i]])

for i in range(1, n+1):
    for j in range(1, cost+1):
        c = thing[i][0]
        n = thing[i][1]

        if j < c:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-c]+n)

print(d[n][cost])


n,k=map(int,input().split())
graph=[]
for i in range(n):
    w,v=map(int,input().split())
    graph.append([w,v])

# k무게 만큼의 배열 생성
dp=[0]*(k+1)
for item in graph:
    w,v=item
    # k번째부터 뒤로 확인하며 dp테이블에 값을 대입하기 위해
    for i in range(k,w-1,-1):
        # k에서 w만큼 뺀 위치의 값이 잇다면 그 값과 현재 꺼낸 물건의 가치 값을 더한 것과 기존것과 비교
        dp[i]=max(dp[i],dp[i-w]+v)
print(dp[k])

0 01 012 0123 01234 01234
1 12 123 1234 
2 23 234
3 34 
4

# cost = [10,20,30,40,50]
# num = [1, 2, 4, 8, 16] -> max_num
# max_cost = 70

# weight = [20,40,50,60,70]
# value = [20,30,50,2,10] -> max_value
# max_weight = 100

    length=len(cost)
    array=[]
    cur=x
    for i in range(length-1,-1,-1):
        if cost[i]<=cur:
            cur-=cost[i]
            array.append(i)
    result=0
    for data in array:
        result+=(2**data)
        
    return result%(int(1e9)+7)