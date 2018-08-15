import sys
nums=input().split(',')
if len(nums)!=12:
    print('0')
    sys.exit()
#for m1 and m2 #################### Month
m1=10
m2=10
m3=10
m4=10
if '1' in nums:
    m1=1
    nums.remove('1')
    if '2' in nums:
        m2=2
        nums.remove('2')
    elif '1' in nums:
        m2=1
        nums.remove('1')
    elif '0' in nums:
        m2=0
        nums.remove('0')
    else:
        nums.append('1')

if m2==10:   
    if '0' in nums:
        m1=0
        nums.remove('0')
        m2=max(nums)
        nums.remove(m2)
    
    else:
        print("0")
        sys.exit()
################################# Date

if '3' in nums:
    m3=3
    nums.remove('3')
    if '1' in nums:
        m4=1
        nums.remove('1')
    elif '0' in nums:
        m4=0
        nums.remove('0')
    else:
        nums.append('3')
        
if m4==10:
    
    if '2' in nums:
        m3=2
        nums.remove('2')
        m4=max(nums)
        nums.remove(m4)
    elif '1' in nums:
        m3=1
        nums.remove('1')
        m4=max(nums)
        nums.remove(m4)
    elif '0' in nums:
        m3=0
        nums.remove('0')
        m4=max(nums)
        nums.remove(m4)
########################## time hours 
t1=10
t2=10
if '2' in nums:
    t1=2
    nums.remove('2')
    if '3' in nums:
        t2=3
        nums.remove('3')
    elif '2' in nums:
        t2=2
        nums.remove('2')
    elif '1' in nums:
        t2=1
        nums.remove('1')
    elif '0' in nums:
        t2=0
        nums.remove('0')
    else:
        nums.append('2')

if t2==10:
    if '1' in nums:
        t1=1
        nums.remove('1')
        t2=max(nums)
        nums.remove(t2)
    elif '0' in nums:
        t1=0
        nums.remove('0')
        t2=max(nums)
        nums.remove(t2)
################################  time minutes
t3=10
t4=10
if t1==2 and t2==3:
    j=0
elif '6' in nums:
    t3=6
    nums.remove('6')
    if '0' in nums:
        t4=0
        nums.remove('0')
    else:
        nums.append('6')

if t4==10:
    if '5' in nums:
        t3=5
        nums.remove('5')
        t4=max(nums)
        nums.remove(t4)
    elif '4' in nums:
        t3=4
        nums.remove('4')
        t4=max(nums)
        nums.remove(t4)
    elif '3' in nums:
        t3=3
        nums.remove('3')
        t4=max(nums)
        nums.remove(t4)
    elif '2' in nums:
        t3=2
        nums.remove('2')
        t4=max(nums)
        nums.remove(t4)
    elif '1' in nums:
        t3=1
        nums.remove('1')
        t4=max(nums)
        nums.remove(t4)
    elif '0' in nums:
        t3=0
        nums.remove('0')
        t4=max(nums)
        nums.remove(t4)
else:
    j=0

###
if m1==10 or m2==10 or m3==10 or m4==10 or t1==10 or t2==10 or t3==10 or t4==10:
    print("0")
    
else:
    print(m1,end='')
    print(m2,end='')
    print('/',end='')
    print(m3,end='')
    print(m4,end='')
    print(' ',end='')
    print(t1,end='')
    print(t2,end='')
    print(':',end='')
    print(t3,end='')
    print(t4,end='')
        

