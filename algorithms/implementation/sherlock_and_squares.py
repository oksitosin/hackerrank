from math import *
 
n = int(raw_input())

for test in range(n):
    a, b = map(int, raw_input().split())

    a = ceil(sqrt(a))
    b = floor(sqrt(b))
    
    print int(b - a) + 1