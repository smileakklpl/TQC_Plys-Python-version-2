n=int(input())
if n==0:
    print(0)
while n!=0:
    print(f'{n%10}',end='')
    n=n//10