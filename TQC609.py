matrix1=[]
for word in [1,2]:
    print(f'Enter matrix {word}:')
    for i in range(1,3):
        for j in range(1,3):
            a=int(input(f'[{i}, {j}]:'))
            matrix1.append(a)
for idx in [1,2]:
    print(f'Matrix{idx}:')
    for i in range(0,4):
        if i==2:
            print()
        print(f'{matrix1[i]} ',end='')
        if len(matrix1)>4:
            matrix2=matrix1
            matrix1=matrix1[4:8]
            print()

print('Sum of 2 matrices:')
for i in range(0,4):
    if i==2:
        print()
    print(f'{matrix2[i]+matrix2[i+4]} ',end='')