file=str(input())
word=str(input())
file='data.txt'
word='Kiwi'
with open(file,'r+',encoding="utf-8") as f:
    print("=== Before the deletion")
    data=f.read()
    print(data)
    print("=== After the deletion")
    data=data.replace(word,'')
    print(data)