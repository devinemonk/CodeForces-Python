n = int(input())
a = list(map(int, input().split()))
 
x = y = a[0]
cnt = 0
for i in range(1, n):
    if a[i] < x:
        x = a[i]
        cnt += 1
    if a[i] > y:
        y = a[i]
        cnt += 1
 
print(cnt)
 
