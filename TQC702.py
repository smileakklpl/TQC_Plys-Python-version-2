print('Creat tuple1:')
tuple1=()
num=int(input())
while num !=-9999:
    tuple1+=(num,)
    num=int(input())

print('Creat tuple2:')
tuple2=()
num=int(input())
while num !=-9999:
    tuple2+=(num,)
    num=int(input())
    
tuple1+=tuple2
print(f'Combined tuple before sorting: {tuple1}')
list_=list(tuple1)
list_.sort()
print(f'Combined list after sorting: {list_}')