from collections import deque

def solution(n, k, cmd):
    answer = ['O']*n
    linktable = { i:[i - 1, i + 1] for i in range(n) }
    linktable[0] = [None, 1]
    linktable[n - 1] = [n - 2, None]
    delete_mem = deque()
    selected = k
    
    for i in cmd:
        if i == 'C':
            answer[selected] = 'X'
            prev, next = linktable[selected]
            delete_mem.append((prev,selected,next))
            if next == None:
                selected = linktable[selected][0]
            else : 
                selected = linktable[selected][1]
                
            if prev == None:
                linktable[selected][0] = None
            elif next == None :
                linktable[selected][1] = None
            else:
                linktable[selected][1] = prev
                linktable[selected][1] = next
            
        elif i == 'Z':
            prev, idx, next = delete_mem.pop()
            answer[idx] = 'O'
            if prev == None:
                linktable[next][0] = idx
            elif next == None:
                linktable[prev][1] = idx
            else:
                linktable[next][0] = idx
                linktable[prev][1] = idx
        else :
            insert = i.split(' ')
            if i == 'U':
                for _ in range(int(insert[1])):
                    selected = linktable[selected][0]
            elif i == 'D':
                for _ in range(int(insert[1])):
                    selected = linktable[selected][1]

    return ''.join(answer)