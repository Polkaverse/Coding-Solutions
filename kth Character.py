p=input()
k=[]
q=list(set(p))
for i in range(0,len(q)):
    j=q[i]
    c=p.replace(j, "")
    k.append(c)
    
k.sort()
print(k[0])



