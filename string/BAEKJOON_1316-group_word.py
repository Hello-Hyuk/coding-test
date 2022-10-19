import sys

n = int(sys.stdin.readline())

words = []
cnt = 0
for i in range(n):
    words.append(sys.stdin.readline().strip())
    alpha = []
    alpha.append(words[i][0])
    for a in enumerate(words[i]):
        if len(alpha) == 1:
            alpha.append(words[i][0])       
        else :
            if alpha[len(alpha)-1] != a[1]:
                if a[1] in alpha:
                    break
                else : alpha.append(a[1])
        if a[0]+1 == len(words[i]):
            cnt += 1
    
print(cnt)
        
            
        
        

