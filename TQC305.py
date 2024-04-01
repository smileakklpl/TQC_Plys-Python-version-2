a=int(input())
if a==0:
    print(0)
while a!=0:
    print(int(a%10),end='')
    a=a//10