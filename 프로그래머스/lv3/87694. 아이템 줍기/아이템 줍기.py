from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    visited = [[True for j in range(1001)] for i in range(1001)]
    moves = {'up':(1,0),'down':(-1,0),'right':(0,1),'left':(0,-1)}
    # 사각형 전부 False 변환
    for c1, r1, c2, r2 in rectangle : 
        for i in range(2*r1, 2*r2+1) :
            for j in range(2*c1, 2*c2+1) : 
                visited[i][j] = False
    
    # 사각형 내부 True로 변환하여 테두리만 False로 만들기
    for c1, r1, c2, r2 in rectangle :             
        for i in range(2*r1+1, 2*r2) : 
            for j in range(2*c1+1, 2*c2) :  
                visited[i][j] = True
    
    # 테두리 따라가기 좌표를 2배로하여 겹치지 않게 만들어주기
    cY, cX, iY, iX = 2*characterY, 2*characterX, 2*itemY, 2*itemX
    dq = deque([(cY, cX, 0)])
    while dq : 
        y, x, time = dq.popleft() # 너비 우선 탐색
        visited[y][x] = True 
        
        if (y,x) == (iY,iX) : 
            print(time//2)
            return time//2
        
        for move in moves: 
            ny = y + moves[move][1]
            nx = x + moves[move][0]
            if 0 <= ny < 1001 and 0 <= nx < 1001 and not visited[ny][nx]: 
                dq.append((ny,nx,time+1))
                visited[ny][nx] = True