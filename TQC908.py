file='908.txt'
n=int(input())
collect=[]
with open(file,'r') as f:
    data=f.read()
    line_=data.split()
    for i in line_:
        if line_.count(i)==n:
            print(i,end='\n')
            line_.remove(i)
    f.close()