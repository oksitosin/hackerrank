t = int(raw_input().strip())
for a in range(t):
    n = int(raw_input().strip())

    count = 0
    for i in str(n):
        d = int(i)
        if d!=0 and n%d==0:
            count += 1     
    print count