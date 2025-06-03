#stack:
stack=[]
top=-1
def push(value):
  global top
  stack.append(value)
  top +=1
def pop():
    global top
    if top==-1:
        priny("Stack is empty.nothing to pop.")
        return 
    else:
        stack.pop()
        top-=1
def peek():
    if top ==-1:
        return "Stack is empty.No top element."
    else:
        return f"top element={stack[top]}"
def display():
    if(top==-1):
        print("empty")
    else:
        for i in range(top,-1,-1):
            print(stack[i])
top=-1
push(10)
push(30)
push(50)
push(70)
pop()
pop()
print(peek())
display()


stack=[]
top=-1
def push(value):
  global top
  stack.append(value)
  top +=1
def pop():
    global top
    if top==-1:
        priny("Stack is empty.nothing to pop.")
        return 
    else:
        stack.pop()
        top-=1
def peek():
    if top ==-1:
        return "Stack is empty.No top element."
    else:
        return f"top element={stack[top]}"
def display():
    if(top==-1):
        print("empty")
    else:
        for i in range(top,-1,-1):
            print(stack[i])


while True:
    print("\n---welcome--")
    print("1.push")
    print("2.pop")
    print("3.peek")
    print("4.display all the elements")
    print("5.exit")
    choise=int(input("Enter your choise"))
    if choise==1:
        value=int(input("Enter the element"))
        push(value)
    elif choise==2:
        pop()
    elif choise==3:
        print(peek())
    elif choise==4:
        display()
    else:
        print("exit")
        break

#program:
class queue:
    def init(self,Q,value):
        self.Q=Q
        self.value=value
    def enqueue(self,Q,value):
        return Q.append(value)



#QEUE:
class Queue:
    def init(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        else:
            return "Queue is empty"
    
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return "Queue is empty"

    def display(self):
         if self.is_empty():
            print("Queue is empty")
         else:
            print("Queue elements:")
            for item in self.items:
                print(item, end=" ")
            print()



