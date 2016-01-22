n = int(raw_input().strip())
arr = map(int,raw_input().split())
for i in range(len(arr)):
    if len(arr) == n and 0<=arr[i]<=pow(10,10):
        s = sum(arr)
    else:
        print 'error'
print s