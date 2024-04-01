n=input()
b=0
for i in range(len(n)):
  if n[i].isupper():  
      b=1
if b==1 and len(n)>=8 and n.isalnum():  
    print("Valid password")
else:   
    print("Invalid password")