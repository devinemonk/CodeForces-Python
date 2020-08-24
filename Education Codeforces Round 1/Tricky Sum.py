for i in range(int(input())):
    s=0
    n=int(input())
    s=n*(n+1)
    s=s//2
    for j in range(n):
        k=2**j
        if k>n:
            break
        s-=k
        s-=k
    print(s)
