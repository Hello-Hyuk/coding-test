import sys

n = int(sys.stdin.readline())

words = []
cnt = 0
for i in range(n):
    alpha = []
    words.append(sys.stdin.readline().strip())
    alpha.append(words[i][0])
    for a in words[i][1:]:
        if alpha[len(alpha)-1] != a and a not in alpha:
            alpha.append(a)
            if len(alpha) == len(words[i]):
                cnt += 1
        else : 
            print(f"{a}")
            break

print(cnt)
        
            
        
        

