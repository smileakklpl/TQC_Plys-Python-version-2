def compute(a,x,y):
    for i in range(0,y):
        print(f'{a} '*x)

a=str(input())
x=int(input())
y=int(input())
compute(a, x, y)