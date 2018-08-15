import sys
c=[]
m=[]
nums=input().split(',')
def maximum(m):
        if m==[]:
            print('impossible')
            sys.exit()
        h=max(m)
        k=c.index(h)
        c.remove(c[k])
        m.clear()
        return h
    

for i in nums:
    c.append(int(i))

for i in range(0,9):
    
    if c[i]<=2:
        m.append(c[i])

else:
    h1=maximum(m)
    
if h1==0:
    for i in range(0,8):
        if c[i]<=9:
            m.append(c[i])
    h2=maximum(m)
elif h1==1:
    for i in range(0,8):
        if c[i]<=9:
            m.append(c[i])
    h2=maximum(m)
else:
    for i in range(0,8):
        if c[i]<=4:
            m.append(c[i])
    h2=maximum(m)

    
#print(h2)
for i in range(0,7):
    if c[i]<=5:
        m.append(c[i])
m1=maximum(m)
#print(m1)
for i in range(0,6):
    if c[i]<=9:
        m.append(c[i])
m2=maximum(m)
#print(m2)
for i in range(0,5):
    if c[i]<=5:
        m.append(c[i])
s1=maximum(m)
#print(s1)
for i in range(0,4):
    if c[i]<=9:
        m.append(c[i])
s2=maximum(m)
#print(s2)
if h1==0 and h2==0 and m1==0 and m2==0 and s1==0 and s2==0:
        print("Impossible")

else:
        print(h1,end='')
        print(h2,end='')
        print(':',end='')
        print(m1,end='')
        print(m2,end='')
        print(':',end='')
        print(s1,end='')
        print(s2,end='')


    


