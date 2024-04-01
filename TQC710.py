d = {}
while True:
    key = input('Key: ') 
    if key == 'end':
        break
    d[key] = input('Value: ')
search = input('Search key: ')
print(search in d.keys())