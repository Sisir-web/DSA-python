class Node:
   def __init__(self,data):
      self.data=data
      self.left=None
      self.right=None
      self.height=1

class AVLtree:
   def height(self,node):
      if not node:
         return 0
      else:
         return node.height
   
   def balance(self,node):
      if not node:
         return 0
      else:
        return self.height(node.left) - self.height(node.right)
      
   def right(self,y):
      x=y.left
      t2=x.right

      x.right=y
      y.left=t2

      y.height=1+max(self.height(y.left),self.height(y.right))
      x.height=1+max(self.height(x.left),self.height(x.right))

      return x
   
   def left(self,x):
      y=x.right
      t2=y.left

      y.left=x
      x.right=t2

      y.height=1+max(self.height(y.left),self.height(y.right))
      x.height=1+max(self.height(x.left),self.height(x.right))

      return y
   
   def insert(self,root,key):
      if root is None:
         return Node(key)
      if key<root.data:
         root.left=self.insert(root.left, key)
      elif key>root.data:
         root.right=self.insert(root.right, key)
      else:
         return root
      
      root.height=1+max(self.height(root.left),self.height(root.right))

      balance=self.balance(root)

      if balance>1 and key<root.left.data:
         return self.right(root)
      elif balance<-1 and key>root.right.data:
         return self.left(root)
      elif balance>1 and key>root.left.data:
         root.left=self.left(root.left)
         return self.right(root)
      elif balance<-1 and key<root.right.data:
         root.right=self.right(root.right)
         return self.left(root)
      
      return root
      
   def preorder(self,root):
      if root:
         print(root.data, end=" ")
         self.preorder(root.left)
         self.preorder(root.right)

a=AVLtree()
root=None
datas=[10,20,30,40,50,25]
for data in datas:
   root=a.insert(root,data)

print()
print("Preorder: ")
a.preorder(root)


         