s=input()+input()
s=s.upper()
d={}
for i in range(ord('A'),ord('Z')+1):
    d[chr(i)]=0
for i in s:
    d[i]+=1
c=input()

for i in c:
    d[i]-=1
for i in d:
    if d[i]!=0:
        print("NO")
        exit()
print("YES")    
