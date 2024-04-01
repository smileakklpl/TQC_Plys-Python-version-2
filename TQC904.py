height=[]
weight=[]

maxh=0 
maxw=0 

with open('read.txt') as file:
    line=file.readlines()
    for x in line:
        print(x)
        ss=x.split(" ")
        height.append(eval(ss[1]))
        weight.append(eval(ss[2]))

        if (eval(ss[1])>maxh):
            maxh=eval(ss[1])
            hname=ss[0]

        if (eval(ss[2])>maxw):
            maxw=eval(ss[2]) 
            wname=ss[0] 
  
avgh=sum(height)/len(height)
avgw=sum(weight)/len(weight)

print("Average height: {:.2f}".format(avgh))
print("Average weight: {:.2f}".format(avgw))
print("The tallest is {} with {:.2f}cm".format(hname,maxh))
print("The heaviest is {} with {:.2f}kg".format(wname,maxw))
