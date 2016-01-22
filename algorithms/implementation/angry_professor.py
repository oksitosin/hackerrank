test_cases = int(raw_input().strip())

if 1 <= test_cases <= 10: 
    
    for a in range(test_cases):
        n,k = raw_input().strip().split(' ')
        n,k = [int(n),int(k)]
        
        if 1 <= n <= 1000 and 1 <= k <= n:
            arrival = map(int,raw_input().strip().split(' '))
            
        for ai in arrival:
            if -100 <= ai <= 100 and len(arrival) == n:
                late = []
                ontime = []
                
                for t in arrival:
                    if t > 0:
                        late.append(t)
                    else:
                        ontime.append(t)

        if len(ontime) < k:
            print 'YES'
        else:
            print 'NO'