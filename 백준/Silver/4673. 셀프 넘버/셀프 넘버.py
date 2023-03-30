num = "1"
visited = [False] * 10001
while num != "10001":
    tmp = int(num)
    for i in num:
        tmp += int(i)
    if tmp <= 10000 and not visited[tmp]:
        visited[tmp] = True
    num = str(int(num)+1)

for i in range(1,len(visited)):
    if visited[i] == False:
        print(i)