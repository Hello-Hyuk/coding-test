import sys

n = int(sys.stdin.readline())
move = []
ball = 1

for _ in range(n):
    move = (list(map(int,sys.stdin.readline().split())))
    if ball in move:
        ball = move[1] if ball == move[0] else move[0]
print(ball)
