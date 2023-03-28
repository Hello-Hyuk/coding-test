import sys
input = sys.stdin.readline

N= int(input())

num_list = []
for _ in range(N):
    num_list.append(int(input()))
    
answer = []
minus = []
one = []
zero = []
plus = []
for i in num_list:
        if i == 1:
            one.append(i)
        elif i == 0:
            zero.append(i)
        elif i > 0:
            plus.append(i)
        elif i < 0:
            minus.append(i)
answer.append(sum(one))
plus.sort(reverse=True)
minus.sort()
#print(plus,minus)
if len(plus)%2==1:
    answer.append(plus.pop())
if len(minus)%2==1:
    tmp = minus.pop()
    if not zero:
        answer.append(tmp)
p_flag, m_flag = -1,-1
p_tmp,m_tmp = 0, 0

for p in plus:
    if p_flag == -1:
        p_tmp = p
    elif p_flag == 1:
        #print(f"answer.append({p_tmp} * {p})")
        answer.append(p_tmp * p)
    p_flag *= -1
    
for m in minus:
    if m_flag == -1:
        m_tmp = m
    elif m_flag == 1:
        #print(f"answer.append({m_tmp} * {m})")
        answer.append(m_tmp * m)
    m_flag *= -1
#print(answer)
print(sum(answer))