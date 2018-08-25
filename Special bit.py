c=[]

n,q=map(int,input().split(' '))
nums=input().split(' ')
for i in nums:
    x=int(i)
    count = 0
   
    
    while (int(x)!=0):
     
        
        x = (int(x) & (int(x) << 1))
  
        count=count+1
     
    c.append(count)

for j in range(0,q):
    count=0
    l,r=map(int, input().split(' '))
    for k in range(l-1,r):
        if c[k]>=2:
            count=count+1
    print(count)
