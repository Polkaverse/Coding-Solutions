# Python program to display No of  prime numbers within an interval
p=int(input())
for i in range(0, p):
# change the values of lower and upper for a different result
    lower , upper = map(int, input().split(" "))

    count=0

    print("Total Prime numbers between",lower,"and",upper,"are:")

    for num in range(lower,upper + 1):
       # prime numbers are greater than 1
       if num > 1:
           for i in range(2,num):
               if (num % i) == 0:
                   break
           else:
               count=count+1
    print(count)
