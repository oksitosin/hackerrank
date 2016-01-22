from __future__ import division

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split())
neg = []
pos = []
zero = []
if n == len(arr):
    for el in arr:
        if el > 0:
            pos.append(el)
        elif el < 0:
            neg.append(el)
        else:
            zero.append(el)

    print '{0:.6f}'.format(len(pos)/len(arr))
    print '{0:.6f}'.format(len(neg)/len(arr))
    print '{0:.6f}'.format(len(zero)/len(arr))