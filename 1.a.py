# Enter your code here
amount=5000
wd=int(input("money:"))
if(wd<amount):
    bal=amount-wd
    print(bal)
else:
    print("insufficient")


#PRINT EVEN NUMBER:
for i in range(0,50):
    if(i%2==0):
        print(i,end=" ")
        
        
#INFINITE LOOP USING WHILE:
i=100
while(i>0):
    i=i-5
    print(i,end=" ")
    i=i+5


