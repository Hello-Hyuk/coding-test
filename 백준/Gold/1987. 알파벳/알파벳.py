import sys
input = sys.stdin.readline

def bfs():
    #dq = deque([[0,0,board[0][0]]])
    global answer
    dq = set([(0,0,board[0][0])])
    while dq:
        r,c,alpha = dq.pop()
        answer = max(answer,len(alpha))
        for move in moves:
            dr = r + moves[move][0]
            dc = c + moves[move][1]
            if 0 <= dr < R and 0 <= dc < C and board[dr][dc] not in alpha:
                next_alpha = alpha + board[dr][dc]
                dq.add((dr,dc,next_alpha))
                
R, C = map(int,input().split())
board = []
for _ in range(R):
    board.append(input().strip())
moves = {'up':(-1,0),'right':(0,1),'down':(1,0),'left':(0,-1)}
answer = 1

bfs()
print(answer)