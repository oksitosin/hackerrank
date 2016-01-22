n = int(raw_input())
arr = map(int, raw_input().split())
arr.sort(reverse=True)

while len(arr) > 0:
    print len(arr)
    block_cut = arr.pop()
    while len(arr) > 0 and arr[-1] <= block_cut:
        arr.pop()