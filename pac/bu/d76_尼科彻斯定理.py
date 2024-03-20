n = int(input())
c = []
for i in range(n*(n-1)+1,n*(n+1),2):
    c.append(i)
for i in c:
    if i == c[-1]:
        print(i)
    else:
        print(i,end='+')
