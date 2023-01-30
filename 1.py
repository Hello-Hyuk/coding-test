#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'solution' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER x
#  2. INTEGER y
#  3. INTEGER z
#  8 7 5
#  
#1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
def solution(x, y, z):
    # Write your code here
    ##차이와 z의 관계 
    # 차이 > z
    diff = abs(x-y)
    if diff > z:
        return -1
    # 차이 == z
    elif diff == z:
        return max(x,y)
    # 차이 < z
    else :
        ## x, y 차이, z와의 관계
        if x==y:
            # 홀수 일때 불가능
            if z%2 == 1:
                return -1
            # 짝수일 때
            elif z%2 == 0 :
                return x+(z//2)
        elif x>y:
            #123456789 1011 12 13 14 15 16 17 18 19 20
            # 5 8 
            # x y 간격이 홀수 이고 z가 짝수
            if diff%2 == 1:
                if z%2 == 0:
                    return -1
                elif z%2 == 1:
                    return x + (z-diff)//2
            elif diff%2 == 0:
                if z%2 == 0:
                    return x + (z-diff)//2
                elif z%2 == 1 :
                    return -1
        # if   4  6  6    5-8 이상 홀수 가능 짝수 불가능
        elif x<y:
            if diff%2 == 1:
                if z%2 == 0:
                    return -1
                elif z%2 == 1:
                    return y + (z-diff)//2
            elif diff%2 == 0:
                if z%2 == 0:
                    return y + (z-diff)//2
                elif z%2 == 1:
                    return -1
                    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x = int(input().strip())

    y = int(input().strip())

    z = int(input().strip())

    result = solution(x, y, z)

    fptr.write(str(result) + '\n')

    fptr.close()
