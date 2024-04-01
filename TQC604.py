m=[0]*100
for i in range(10):
   n=int(input())
   m[n]+=1
print(m.index(max(m)))  #取得位址
print(max(m))