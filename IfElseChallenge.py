import math
import os
import random
import re
import sys

def evaluate(n):
    if n % 2 == 0:
        if n in range (2, 6):
            print("Not Weird")
        
        elif n in range (6, 21):
            print("Weird")
        
        else:
            print("Not Weird")
    else:
        print("Weird")
    
if __name__ == '__main__':
    n = int(input().strip())
    evaluate(n)