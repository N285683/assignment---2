a=[(1,2),(2,1),(5,5),(3,2),(2,3)]
b=[i[-1] for i in a]
c=[]
l=0
for j in a:
    for k in a:
        if k[1]==min(b)+l:
            c.append(k)
            l+=1
        a=[f for f in a if f not in c]
print(c)
