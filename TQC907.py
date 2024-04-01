file='readd.txt'
line=word=char=0
with open(file,'r') as f:
    for lines in f:
        line+=1
        word+=len(lines.split())
        char+=len(lines.replace(' ',''))
    f.close()
print(line)
print(word)
print(char)