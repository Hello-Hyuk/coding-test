def solution(n):
    dx = [0, 1, -1]
    dy = [1, 0 ,-1]
    x,y,mode = 0,0,0
    tri = [[0 for _ in range(i+1)] for i in range(n)]
    visited = [[False for _ in range(i+1)] for i in range(n)]
    tri[y][x] = 1
    visited[y][x] = True
    final_num = 0
    for i in range(1,n+1):
        final_num += i
        
    for i in range(2,final_num+1):
        try : 
            if y +dy[mode] >= n or x +dx[mode] >= n or visited[y +dy[mode]][x +dx[mode]] == True:
                mode += 1
                mode %= 3
        except IndexError as I:
            mode += 1
            mode %= 3
            
        ny = y +dy[mode]
        nx = x +dx[mode]
        
        if visited[ny][nx] == False: 
            tri[ny][nx] = i
            visited[ny][nx] = True
            x = nx
            y = ny
    
    
    return sum(tri, [])