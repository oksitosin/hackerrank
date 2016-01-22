n = int(raw_input())
arr = map(int,raw_input().split())
if len(arr) == n:
    s = sum(arr)
    print s
else:
    print 'add more' 