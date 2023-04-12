import sys
input = sys.stdin.readline
M = int(input())
SET = set()
answer = []
for _ in range(M):
    cmd_num = input().rstrip().split(" ")
    if len(cmd_num) == 2:
        cmd, num = cmd_num
    else :
        cmd = cmd_num[0]
        num = 0
    num = int(num)
    if cmd == "add":
        SET.add(num)
    elif cmd == "remove":
        if num in SET:
            SET.remove(num)
    elif cmd == "check":
        if num in SET:
            print(1)
        else : 
            print(0)
    elif cmd == "toggle":
        if num in SET:
            SET.remove(num)
        else :
            SET.add(num)
    elif cmd == "all":
        SET = set(range(1,21))
    elif cmd == "empty":
        SET = set()