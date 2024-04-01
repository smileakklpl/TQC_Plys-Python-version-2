set1 = set()
set2 = set()
set3 = set()

print('Input to set1:')
for i in range(5):
    a=int(input())
    set1.add(a)
    
print('Input to set2:')
for i in range(3):
    a=int(input())
    set2.add(a)

print('Input to set3:')
for i in range(9):
    a=int(input())
    set3.add(a)
    
print('set2 & set1 ',set2.issubset(set1))
print('set3 % set1',set3.issuperset(set1))