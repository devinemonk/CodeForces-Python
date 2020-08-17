for i in range(int(input())):
    s=input()
    a=[]
    l=len(s)-1
    for j in range(len(s)):
        if s[j]!='0':
            a.append(int(s[j])*(10**(l-j)))
    print(len(a))
    print(*a)
