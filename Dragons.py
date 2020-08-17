s,n=map(int,input().split())
x=[]
for i in range(n):
    a,b=map(int,input().split())
    x.append((a,b))
x.sort()
for i in range(n):
    a,b=x[i][0],x[i][1]
    if s>a:
        s+=b
    else:
        print("NO")
        exit()
print("YES")
