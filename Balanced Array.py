for i in range(int(input())):
    n=int(input())
    if n%4==0:
        a=[]
        n=n//2
        print("YES")
        for j in range(1,n+1):
            a.append(2*j)
        #a.append(n)
        for j in range(1,n):
            a.append(2*j-1)
        a.append(3*n-1)
        print(*a)
    else:
        print("NO")
