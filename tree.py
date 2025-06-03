# Enter your code here
class Node:
    def __init__(self):
        self.left=None
        self.right=None
        self.data=None
    def inorder_traversal(self,Node):
        if Node:
            self.inorder_traversal(Node.left)
            print(Node.data, end=" ")
            self.inorder_traversal(Node.right)
    def preorder_traversal(self,Node):
        if Node:
            print(Node.data, end=" ") 
            self.preorder_traversal(Node.left)
            self.preorder_traversal(Node.right)
    def postorder_traversal(self,Node):
        if Node:
            print(Node.data, end=" ") 
            self.postorder_traversal(Node.left)
            self.postorder_traversal(Node.right) 
    def sum_of_nodes(self,Node):
        if Node is None:
            return 0
        return Node.data + self.sum_of_nodes(Node.left)+self.sum_of_nodes(Node.right)
    def count_nodes(self,Node):
        if(Node is None):
            return 0
        return node.data + self.count_nodes(Node.left) + self.count_nodes(Node.right)
            
tree=Node()
tree.data=1 
tree.left=Node()  
tree.left.data=2    
tree.right=Node()
tree.right.data=3
tree.left.left=Node()
tree.left.left.data=4
tree.left.right=Node()
tree.left.right.data=5
tree.right.left=Node()
tree.right.left.data=6
tree.right.right=Node()
tree.right.right.data=7
print("\ninorder traversal of binary tree is:")
tree.inorder_traversal(Node=tree)
print("\npreorder traversal of binary tree is:")
tree.preorder_traversal(Node=tree)
print("\npostorder traversal of binary tree is:")
tree.postorder_traversal(Node=tree)
print("\nSum of all nodes in binary tree is:")
print(tree.sum_of_nodes(Node=tree))
print("\nSum of all nodes in left subtree tree is:")
print(tree.sum_of_nodes(Node=tree.left))
print("\nSum of all nodes in right subtree tree is:")
print(tree.sum_of_nodes(Node=tree.right))
print("\n No of nodes in the left sub tree")
print(tree.count_nodes(Node=tree.left))
print("\n No of nodes in the right sub tree")
print(tree.count_nodes(Node=tree.right))
print("\n No of nodes in the given tree are:")
print(tree.count_nodes(Node=tree))









You are given an integer array of size N, representing jars of chocolates. Three
students A, B, and C respectively, will pick chocolates one by one from each chocolate
jar, till the jar is empty, and then repeat the same with the rest of the jars. Your task
is to fine and return an integer value representing the total number of chocolates that
student A will have, after all the chocolates have been picked from all the jars.
Note: Once a jar is done A will start taking the chocolates from the new jar.
Input Format :
input1: An integer array representing the quantity of chocolates in each jar.
input2: An integer value N representing the number of jars.
Output Format:
Return an integer value representing the total number of chocolates that student A
will have, after all the chocolates are picked.
Example:
Input:
10 20 30
3
Output:
21










Paul is given an array A of length N. He must perform the following Operations on the
array sequentially:
* Choose any two integers from the array and calculate their average.
* If an element is less than the average, update it to 0. However, if the element is
greater than or equal to the average, he need not update it.
Your task is to help Paul find and return an integer value, representing the minimum
possible sum of all the elements in the array by performing the above operations. Note: An exact average should be calculated, even if it results in a decimal.

Input Format:
input1: An integer value N, representing the size of the array A.
input2: An integer array A.
Output Format:
Return an integer value, representing the minimum possible sum of all the elements
in the array by
Sample Input
5
1 2 3 4 5
Sample Output
5
CODE : arr=list(map(int,input().split()))
arr.sort()
a1=arr[1]
a2=arr[2]
sum=0
avg=(a1+a2)/2
for i in range(len(arr)):
    if arr[i]<avg:
        arr[i]+0
for i in range(len(arr)):
    sum+=arr[i]
print(sum)








(3)'''The function accepts two positive integers ‘r’ and ‘unit’ and a positive integer array ‘arr’ of size ‘n’ as its argument ‘r’ represents the number of rats present in an area, ‘unit’ is the amount of food each rat consumes and each ith element of array ‘arr’ represents the amount of food present in ‘i+1’ house number, where 0 <= i

Note:

Return -1 if the array is null
Return 0 if the total amount of food from all houses is not sufficient for all the rats.
Computed values lie within the integer range.
Example:

Input:

r: 7
unit: 2
n: 8
arr: 2 8 3 5 7 4 1 2
Output:

4

Explanation:
Total amount of food required for all rats = r * unit

= 7 * 2 = 14.

The amount of food in 1st houses = 2+8+3+5 = 18. Since, amount of food in 1st 4 houses is sufficient for all the rats. Thus, output is 4.
CODE : r=int(input())
units=int(input())
n=int(input())
arr=list(map(int,input().split()))

food_required=r*units
if(arr==0):
    print(-1)
for i in range(n):
    food_required=food_required-arr[i]
    if(food_required<0):
        break
if(food_required>0):
    print(0)
print(abs(food_required)) 





(4).You are given a function.
int CheckPassword(char str[], int n);
The function accepts string str of size n as an argument. Implement the function which returns 1 if given string str is valid password else 0.
str is a valid password if it satisfies the below conditions.

– At least 4 characters
– At least one numeric digit
– At Least one Capital Letter
– Must not have space or slash (/)
– Starting character must not be a number
Assumption:
Input string will not be empty.

Example:

Input 1:
aA1_67
Input 2:
a987 abC012

Output 1:
1
Output 2:
0 
CODE: s=input()
dc=s[5:9]
s1=s[0:5]
if(len(s)==10 and s[-1].isalpha() and dc.isdigit() and s1.isalpha()):
    print("valid")
else:
    print("invalid")
    


(5) :Write a Python program that takes two integers n and m as input and computes a checksum using the following logic:
•	Count how many numbers from 1 to m are not divisible by n.
•	Count how many numbers from 1 to m are divisible by n.
•	Return the difference between these two counts:
not_divisible_count - divisible_count
________________________________________
Input Format:
•	First line: An integer n (the divisor)
•	Second line: An integer m (the upper bound)
________________________________________
Output Format:
•	A single integer representing the checksum
________________________________________
Example Input
n = 3
m = 10
Example Output:
4
Explanation:
Numbers from 1 to 10:
Divisible by 3 → 3, 6, 9 → count = 3
Not divisible by 3 → 1, 2, 4, 5, 7, 8, 10 → count = 7
Checksum = 7 - 3 = 4

CODE: n=int(input())
m=int(input())
count_divisable=0
count_not_divisable=0
for i in range(1,m+1):
    # not divisable by not n 
    if(i % n != 0):
        count_not_divisable += 1 
    else:
        count_divisable += 1 
print(abs(count_divisable - count_not_divisable))        
