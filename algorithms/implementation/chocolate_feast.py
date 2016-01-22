t = int(raw_input().strip())
for a in range(t):
    n,c,m = raw_input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    num_chocolates = n/c
    num_wrappers = num_chocolates
    while num_wrappers >= m:
        add_choco = num_wrappers / m
        leftover_wrappers = num_wrappers % m
        num_wrappers = add_choco + leftover_wrappers
        num_chocolates += add_choco
        
    print num_chocolates