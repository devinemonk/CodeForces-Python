n=10**6
prime = [1 for i in range(n+1)]
p = 2
while (p * p <= n):
    if (prime[p] == 1): 
        for i in range(p * p, n+1, p): 
            prime[i] = 0
    p += 1
n=int(input())
a=n//2
while(prime[a]==1 or prime[n-a]==1):
    a-=1
print(a,end=" ")
print((n-a))
