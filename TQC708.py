dic1={}
dic2={}
print('Creat dict1:')
key='hi'
while 1:
    key=str(input('Key:'))
    if key=='end':
        break
    value=str(input('Value:'))
    dic1[key]=value

print('Creat dict2:')
key='hi'
while 1:
    key=str(input('Key:'))
    if key=='end':
        break
    value=str(input('Value:'))
    dic2[key]=value
    
dic1.update(dic2)
for i in dic1.keys():
    print(f'{i}: {dic1[i]}')