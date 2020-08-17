n,l=map(int,input().split())
s='#'
f=0
for i in range(n):
    if i%2==0:
        print(s*l)
    else:
        f+=1
        if f%2==0:
            print('#'+'.'*(l-1))
        else:
            print('.'*(l-1)+s)
        
            
        
