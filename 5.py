#NSERTING LINKED LIST:
class Node:
    def init(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def init(self):
        self.head = None              #starting poing of linked list
    def insert(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next    #moves temp node
            temp.next = new_node
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp =temp.next
        print("None")
ll=LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.display()



#SUM OF THE LINKED LIST:
class Node:
    def init(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def init(self):
        self.head = None              #starting poing of linked list
    def insert(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next    #moves temp node
            temp.next = new_node
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp =temp.next
        print("None")
    def add_ll(self):
        temp=self.head
        sum=0
        while temp:
            sum=sum+temp.data
            temp=temp.next
        return sum
ll=LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.display()
print("sum of elements in the linked list")
ans=ll.add_ll()
print(ans)





#INSERT THE ELEMENT AT THE BEGINING:
class Node:
    def init(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def init(self):
        self.head = None              #starting poing of linked list
    def insert_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next    #moves temp node
            temp.next = new_node
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp =temp.next
        print("None")
    def add_ll(self):
        temp=self.head
        sum=0
        while temp:
            sum=sum+temp.data
            temp=temp.next
        return sum
    def count(self):
        pass
    def insert_begining(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
ll=LinkedList()
ll.insert_end(10)
ll.insert_begining(7000)
ll.insert_end(20)
ll.insert_end(30)
ll.insert_end(40)
ll.display()
print("sum of elements in the linked list")
ans=ll.add_ll()
print(ans)
