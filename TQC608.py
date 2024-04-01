list=[]
for i in range(9):
    n=int(input())
    list.append(n)
print(f'Index of the largest number {max(list)} is: ({list.index(max(list))//3}, {(list.index(max(list))%3)})')