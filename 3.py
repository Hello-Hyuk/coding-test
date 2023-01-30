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
# The function accepts INTEGER_ARRAY box as parameter.
#
def calc_box(box):
    tmp = 0
    ref = sum(box) // len(box)
    for i in enumerate(box):
        if i[0] == len(box)-1:
            if i[1]+tmp > ref:
                return ref + 1
            elif i[1]+tmp == ref:
                return ref
            else :
                return max(box) 
        else :
            if i[1]+tmp >= ref:
                tmp = (i[1] + tmp) - ref
            else : return max(box) 
            #calc_box(box[i+1:])
            
def solution(box):
    # Write your code here
    box.reverse()
    return calc_box(box)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    box_count = int(input().strip())

    box = []

    for _ in range(box_count):
        box_item = int(input().strip())
        box.append(box_item)

    result = solution(box)

    fptr.write(str(result) + '\n')

    fptr.close()
