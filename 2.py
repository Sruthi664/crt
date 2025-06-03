# Enter your code here
#list
lst=[-12,13,-15,14,17]
arr=[]
arr1=[]
for i in range(0,len(lst)):
    if(lst[i]>0):
        arr.append(lst[i])
    else:
        arr1.append(lst[i])
print(arr)
print(arr1)


#STRINGS:
s="mouni12345"
count=0
for i in s:
    if(i.isdigit()):
        count=count+1
print(count)


#COUNT SPACE:
S="hello world hello"
count=0
for i in S:
    if(i==' '):
        count+=1
print(count)



#Sum of even elements:
a=[1,2,3,4,5,6]
sum=0
for i in a:
    if(i%2==0):
        sum=sum+i
print(sum)




#Variable length argument:
def add(*args):
    return sum(args)
ans=add(10,20,300)
print(ans)



#Print natural number:
def natural (n):
    if(n==5):
        return 5
    else:
        print(n,end=" ")
        return natural(n+1)
ans=natural(1)
print(ans)
