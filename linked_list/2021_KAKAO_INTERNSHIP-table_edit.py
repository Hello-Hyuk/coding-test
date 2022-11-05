def solution(n, k, cmd):
    cur = k
    table = { i:[i - 1, i + 1] for i in range(n) }
    answer = ['O'] * n
    table[0] = [None, 1]
    table[n - 1] = [n - 2, None]
    stack = []
    for c in cmd:
        if c == "C":
            # 삭제
            answer[cur] = 'X'
            prev, next = table[cur]
            stack.append([prev, cur, next])
            if next == None:
                cur = table[cur][0]
            else:
                cur = table[cur][1]
            if prev == None:
                table[next][0] = None
            elif next == None:
                table[prev][1] = None
            else:
                table[prev][1] = next
                table[next][0] = prev
 
        elif c == "Z":
            # 복구
            prev, now, next = stack.pop()
            answer[now] = 'O'
            if prev == None:
                table[next][0] = now
            elif next == None:
                table[prev][1] = now
            else:
                table[next][0] = now
                table[prev][1] = now
 
        else:
            # 커서 이동
            c1, c2 = c.split(' ')
            c2 = int(c2)
            if c1 == 'D':
                for _ in range(c2):
                    cur = table[cur][1]
            else:
                for _ in range(c2):
                    cur = table[cur][0]
    return ''.join(answer)




# my
import numpy as np
from collections import deque

def solution(n, k, cmd):
    answer = ""
    gt_table = []
    linktable = { i:[i - 1, i + 1] for i in range(n) }
    linktable[0] = [None, 1]
    linktable[n - 1] = [n - 2, None]
    print(linktable)
    delete_mem = deque()
    delete_mem_idx = deque()
    selected = k
    for i in enumerate(range(n)):
        gt_table.append(i)
    table = np.array(gt_table)
    gt_table_np = np.array(gt_table)
    for i in cmd:
        insert = (i.split(" "))
        if insert[0] == 'U':
            selected -= int(insert[1])
        elif insert[0] == 'D':
            selected += int(insert[1])
        elif insert[0] == 'C':
            delete_mem.append(table[selected])
            delete_mem_idx.append(selected)
            table = np.delete(table,selected,axis=0)
            table[selected:,0] -= 1 
        elif insert[0] == 'Z':
            restore = delete_mem.pop()
            restore_idx = delete_mem_idx.pop()
            table[restore_idx:,0] += 1
            table = np.insert(table,restore_idx,restore,axis=0)
    for i in range(n):
        if i in table[:,1]:
            answer += 'O'
        else :
            answer += 'X'
    return answer



#######
import numpy as np
from collections import deque

def solution(n, k, cmd):
    answer = ['O']*n
    gt_table = []
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