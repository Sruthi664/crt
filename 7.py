# Enter your code here
arr=list(map(int,input().split()))
arr.sort()
a1=arr[-1]
a2=arr[-2]
sum=0
avg=(a1+a2)/2
for i in range(len(arr)):
    if arr[i]<avg:
        arr[i]=0
for i in range(len(arr)):
    sum+=arr[i]
print(sum)


 
r=7
unit=2
arr=[2, 8, 3, 5, 7, 4, 1, 2]
food_req=r*unit
for i in range(len(arr)):
    food_req=food_req-arr[i]
    if (food_req<0):
        break
print(abs(food_req))


s=input()
dc=s[5:9]
s1=s[0:5]
if(len(s)==10 and s[-1].isalpha() and dc.isdigit() and s1.isalpha()):
    print("valid")
else:
    print("invalid")



n = int(input())  
m = int(input())  
count_divisible = 0
count_not_divisible = 0
for i in range (1,m+1):
    if(i%n!=0):
        count_not_divisible+=1
    else:
        count_divisible+=1
print(abs( count_not_divisible-count_divisible))


 
for i in range(4):
    for j in range(4):
        if(i==j):
            print("$",end=" ")
        else:
            print("*",end=" ")
    print()



for i in range(1,5):
    for j in range(1,5):
        if i == 1 or i == 4 or j == 1 or j == 4:
                print("*", end=" ")
        else:
                print(" ", end=" ")
    print()


 for i in range(1,5):
    for j in range(1,5):
        if i == 1 or i == 4 or j == 1 or j == 4:
                print(j+ (i-1),end=" ")
        else:
                print(" ", end=" ")
    print()


for i in range(1,5):
    for j in range(1,5):
        if (i<j):
            print(" ", end=" ")
        else:
            print("*",end=' ')
    print()


for i in range(1,5):
    for j in range(1,5):
        if (i>j):
            print(" ", end=" ")
        else:
            print("*",end=' ')
    print()
    

for i in range(1,5):
    for j in range(1,5):
        if (i<j):
            print(" ", end=" ")
        else:
            print("*",end=' ')
    print()
    
for i in range(1,5):
    for j in range(1,5):
        if (i+j>=5):
            print("*", end=" ")
        else:
            print(" ",end=' ')
    print()
    
for i in range(1,5):
    for j in range(1,5):
        if (i+j<=5):
            print("*", end=" ")
        else:
            print(" ",end=' ')
    print()
    
    
for i in range(4,0,-1):
   print("*"*i)
   
   
   
for i in range(1,5):
    for j in range(1,5):
        if (i<j):
            print(" ", end=" ")
        else:
            print(j,end=' ')
    print()


