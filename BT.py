class Node:
   def __init__(self,left=None,data=None,right=None):
      self.left=None
      self.data=data
      self.right=None

class bt:
   def __init__(self):
      self.root=None

   def empty(self):
      return self.root == None
   
   def insert(self,data):
      new_node=Node(data=data)
      if self.empty():
         self.root=new_node
         return
      
      queue=[self.root] #root node in queue first 
      while queue:
         current=queue.pop(0) #we will check the left and right of the root node and dequeue the root ,enqueue[root.left,root.right]

         if current.left is None: #if there is no node in the left insert the new_node there .
            current.left=new_node
            return
         else:
            queue.append(current.left) #This will help to check whether there is node or not subtree on the left of the root node and enqueue it to the queue.

         if current.right is None: #after traversing the left side it will check the rigth node now and if empty it will add the new_node there in the right
            current.right=new_node
            return
         else:
            queue.append(current.right) #This will help to check whether there is node or not subtree on the right of the root node and enqueue it to the queue.

   def preorder(self,node): #This is the preorder traversal 
      if node:
         print(node.data,end=" ")
         self.preorder(node.left)
         self.preorder(node.right)

   def inorder(self,node):
      if node:
         self.inorder(node.left)
         print(node.data,end=" ")
         self.inorder(node.right)

   def postorder(self,node):
      if node:
         self.postorder(node.left)
         self.postorder(node.right)
         print(node.data,end=" ")

b = bt()
b.insert(1)
b.insert(2)
b.insert(4)
b.insert(5)
b.insert(3)
b.insert(6)

b.preorder(b.root)
print()
b.inorder(b.root)
print()
b.postorder(b.root)

         

         

