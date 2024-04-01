def compute(x,y):
    final=0
    for i in range(1,max([x,y])+1):
        if x%i==0 and y%i==0:
            final=i
    return final

print(compute(30, 10))