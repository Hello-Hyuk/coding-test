import sys

n = int(sys.stdin.readline())

p = []
for i in range(n):
    age, name = map(str,sys.stdin.readline().split())
    age = int(age)
    p.append((age,name))

p.sort(key = lambda age : age[0])	

for i in p:
    print(i[0], i[1])