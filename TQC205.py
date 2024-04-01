while 1:
    n=str(input())
    if n.isdigit()==True:
        print(f'{n} is number')
    elif n.isalpha()==True:
        print(f'{n} is alpha')
    else:
        print(f'{n} is symbol')