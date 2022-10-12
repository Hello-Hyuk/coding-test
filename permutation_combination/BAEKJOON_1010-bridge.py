import sys
from functools import reduce

n = int(sys.stdin.readline())

def nCr(n, r):
    upper = reduce(lambda x, y : x*y, list(range(n,n-r,-1)),1)
    lower = reduce(lambda x, y : x*y, list(range(r,1,-1)),1)
    return upper // lower

for _ in range(n):
    node = list(map(int, sys.stdin.readline().split()))
    ans = nCr(node[1],node[0])
    print(ans)



## itertools combination 사용시
# from itertools import combinations
# nodes_tmp = []
# nodes = []

# for i in range(len(nodes_tmp)):
#     nodes.append(list(range(nodes_tmp[i][1])))
# # print(nodes)

# for i in range(len(nodes_tmp)):    
#     ans_tmp = []
#     for j in combinations(nodes[i], nodes_tmp[i][0]):
#         ans_tmp.append(j)
#     ans.append(len(ans_tmp))
    
# for a in ans:
#     print(a)
