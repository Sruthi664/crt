# Enter your code here
class Node():
    def init(self):
         self.left=None
         self.right=None
         self.data=None
    def postorder_traversal(self,Node):
        if Node:
           self.postorder_traversal(Node.left)
           self.postorder_traversal(Node.right)
           print(Node.data)
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
tree.postorder_traversal(Node=tree)



class Node():
    def init(self):
         self.left=None
         self.right=None
         self.data=None
    def postorder_traversal(self,Node):
        if Node:
           self.postorder_traversal(Node.left)
           self.postorder_traversal(Node.right)
           print(Node.data)
    def Height(self,Node):
        if Node is None:
            return 0
        else:
            return max(self.Height(Node.left),self.Height(Node.right))+1
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
tree.postorder_traversal(Node=tree)
print(tree.Height(Node=tree))



class Node():
    def init(self):
         self.left=None
         self.right=None
         self.data=None
    def postorder_traversal(self,Node):
        if Node:
           self.postorder_traversal(Node.left)
           self.postorder_traversal(Node.right)
           print(Node.data)
    def count_nodes(self,Node):
        if Node is None:
            return 0
        return 1+self.count_nodes(Node.left)+self.count_nodes(Node.right)
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
tree.postorder_traversal(Node=tree)
print(tree.count_nodes(Node=tree))




