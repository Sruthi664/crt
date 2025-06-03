class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedList:    
    def __init__(self):
        self.head=None  #starting point of linkedlist
    def insert_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next:
                temp=temp.next   #it will move temp node for 
            temp.next=new_node
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("None")
    def add_ll(self):
        temp=self.head
        sum=0
        while temp:
           sum=sum+temp.data
           temp=temp.next
        return sum   
    def count(self):
        count=0
        temp=head
        while(temp):
            count=count+1
            temp=temp.next
        return count
    def insert_beginning(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def delete_beginning(self):
        self.head=self.head.next
    def delete_end(self):
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=None   
    def insert_position(self,pos,data):
        if(pos==0):
            self.insert_beginning(data)
        else:
            new_node=Node(data)
            temp=self.head
            for _ in range(pos-1):
                if temp is None:
                    print("position out of bounds")
                    return
                    
                temp=temp.next
                temp=temp.next.next
              
            new_node.next=temp.next
            temp.next=new_node
    def delete_value(self,value):
        if self.head.data==value:
            self.head=self.head.next
            return
        temp=self.head
        while temp.next and temp.next.data != value:
            temp=temp.next
        if temp.next is None:
            print("value not found")
            return

        
        
ll = linkedList()
ll.insert_beginning(10)
ll.insert_beginning(20)
ll.insert_beginning(30)
ll.display()
ll.insert_position(3,100)
ll.delete_value(20)
ll.display()

print("sum of elements in linked list is ")
ans=ll.add_ll()
print(ans)
