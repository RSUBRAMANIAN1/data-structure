import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    n=len(a)

    a=a[((n+d)%n):]+a[0:((n+d)%n)]
    return a


if __name__ == '__main__':

    nd = input('enter length of array \n enter number of rotations').split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)
    print(*result,sep=' ')

  
   
