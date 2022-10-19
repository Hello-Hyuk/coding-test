import sys

n = int(sys.stdin.readline())
tri = []
for _ in range(n):
    tri.append(list(map(int,sys.stdin.readline().split())))

for i in range(1,n):
    for j in range(len(tri[i])):
        if j == 0:
            tri[i][j] += tri[i-1][j]
        elif j == i:
            tri[i][j] += tri[i-1][j-1]
        else:
            tri[i][j] += max(tri[i-1][j], tri[i-1][j-1])
            
print(max(tri[n-1]))