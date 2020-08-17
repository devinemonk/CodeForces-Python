n,l=map(int,input().split())
a=list(map(int,input().split()))
a.insert(0,1)
s=0
for i in range(1,l+1):
    if (a[i]>=a[i-1]):
        s+=a[i]-a[i-1]
        #print(a[i]-a[i-1])
    else:
        s+=n-a[i-1]+a[i]
        #print(n-a[i-1]+a[i])
print(s)
