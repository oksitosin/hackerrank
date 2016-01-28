def pff():
    
    testcases = int(raw_input())
    
    for i in range(testcases):
        n = int(raw_input())
        div = 2
        
        while div * div <= n:
            while n % div == 0:
                if n == div:
                    break      
                else:
                    n = n/div
            div = div + 1    
        print n

pff() 