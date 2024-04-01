with open('data.dat','w') as file:
    for i in range(5):
        string=str(input())
        file.write(string+'\n')
file.close()

print('The content of "data.dat":')
with open('data.dat','r') as file:
    for i in file:
        print(i)
file.close()