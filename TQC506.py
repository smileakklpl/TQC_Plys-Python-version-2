def compute(a,b,c):
    des=b**2-4*a*c
    if des<0:
        print('Your equation has no root.')
    elif des==0:
        print(-b/2*a)
    else:
        print(f'{(-b+des**(1/2))/(2*a)}, {(-b-des**(1/2))/(2*a)}')
        
a=int(input())
b=int(input())
c=int(input())
compute(a, b, c)