a,b,c,d=map(int,input().split())
s=max(a,b,c,d)
if s!=a:
    print(s-a,end=" ")
if s!=b:
    print(s-b,end=" ")
if s!=c:
    print(s-c,end=" ")
if s!=d:
    print(s-d,end=" ")
