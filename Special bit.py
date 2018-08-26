c=[]
t=[]
n,q=map(int,input().split(' '))
for i in range(0,n):
    t.append(int(input()))
for i in range(0,len(t)):
    input=bin(t[i])
    input=input[2:]
    
     
    c.append(max(map(len, input.split('0'))))
print(c)
for j in range(0,q):
    count=0
    l,r=map(int, input().split(' '))
    for k in range(l-1,r):
        if c[k]>=2:
            count=count+1
    print(count)
