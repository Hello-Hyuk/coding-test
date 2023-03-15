import sys
input = sys.stdin.readline()

T = int(input)
buttons = {'A':300, 'B':60, 'C':10}
answer = []

for button in buttons:
    if T >= buttons[button]:
        times = T//buttons[button]
        answer.append(times)
        T -= buttons[button] * times
    else : 
        answer.append(0)

if T: print(-1)
else : print(*answer)  