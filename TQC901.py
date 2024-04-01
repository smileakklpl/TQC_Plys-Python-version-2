with open('write.txt','w')as file:
    for i in range(5):
        word=str(input())
        file.write(word+'\n')
file.close()