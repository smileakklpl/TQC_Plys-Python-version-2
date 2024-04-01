def compute(n):
    first=1
    last=0
    print(0,end=' ')
    for i in range(0,n-1):
        now=first+last
        print(now,end=' ')
        first=last
        last=now
    

compute(10)