import sys
input = sys.stdin.readline
go = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]

def spring_summer_winter():
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                dead_soil = 0
                tree_ij = {}
                no_soil = False
                for age in sorted(tree[i][j].keys()):
                    total_tree = tree[i][j][age]
                    if no_soil:
                        dead_soil += total_tree * (age//2)
                    elif soil[i][j] >= total_tree*age:
                        soil[i][j] -= total_tree*age
                        tree_ij[age+1] = total_tree
                    else:
                        no_soil = True
                        alive_tree = soil[i][j]//age
                        dead_soil += (total_tree-alive_tree) * (age//2) # 연산 순서 때문에 괄호 꼭 써야함
                        if alive_tree>0:
                            soil[i][j] -= alive_tree*age
                            tree_ij[age+1] = alive_tree
                tree[i][j] = tree_ij
                soil[i][j] += dead_soil
            soil[i][j] += add_soil[i][j]
    
def fall():
    for i in range(n):
        for j in range(n):
            new_tree = 0
            for age in tree[i][j].keys():
                if age%5 == 0:
                    new_tree += tree[i][j][age]
            if new_tree:
                for di,dj in go:
                    ni,nj = i+di,j+dj
                    if 0 <= ni < n and 0 <= nj < n:
                        if 1 in tree[ni][nj]:
                            tree[ni][nj][1] += new_tree
                        else:
                            tree[ni][nj][1] = new_tree

n,m,k = map(int,input().split())
add_soil = [list(map(int,input().split())) for _ in range(n)]
soil = [[5]*n for _ in range(n)]
tree = [[{} for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x,y,z = map(int,input().split())
    tree[x-1][y-1][z] = 1
while k>0:
    k -= 1
    # 1.봄:나이만큼 양분먹고, 나이 1증가
    # 나무 여러개면 어린나무부터 양분먹기
    # 2.여름:죽은 나무 나이//2 가 양분이 됨
    # 4.겨울:로봇이 양분 추가
    spring_summer_winter()
    
    # 3.가을:나이가 5의배수인 나무가 번식
    fall()

ans = 0
for i in range(n):
    for j in range(n):
        ans += sum(tree[i][j].values())
print(ans)