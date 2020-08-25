import sys

def get_array(): return list(map(int, sys.stdin.readline().split()))
def get_ints(): return map(int, sys.stdin.readline().split())
def input(): return sys.stdin.readline().strip('\n')

n,m,k=get_ints()
 
visited=[]
 
for i in range(n):
    visited.append([])
    
    for j in range(m):
        visited[i].append(0)
        
s=0
d={}
def dfs(x,y):
    global s
    s+=1
    #cell=[]
    c=0
    q=[(x,y)]
    while q:
        x,y=q.pop()
        if x>=n or y>=m or x<0 or y<0:
            return 
        if l[x][y]=='*':
            c+=1
            continue
        if visited[x][y]:
            continue
        visited[x][y]=s
        #cell.append((x,y))
        q.append((x+1,y))
        q.append((x-1,y))
        q.append((x,y+1))
        q.append((x,y-1))
    '''   
    for x in cell:
        if visited[x[0]][x[1]]:
            visited[x[0]][x[1]]=c
            
    ''' 
    d[s]=c
 
 
 
 
 
 
l=[]
for i in range(n):
    l.append(input())
for i in range(n):
    for j in range(m):
        if not visited[i][j] and l[i][j]=='.':
            dfs(i,j)
for i in range(k):
    x,y=get_ints()
    x-=1
    y-=1
    print(d[visited[x][y]])
