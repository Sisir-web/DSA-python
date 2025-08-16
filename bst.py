class Node:
   def __init__(self,data):
      self.data=data
      self.left=None
      self.right=None

class BST:

   def insert(self,root,key):
      if root is None:
         return Node(key)
      if key<root.data:
         root.left= self.insert(root.left,key)
      elif key>root.data:
         root.right= self.insert(root.right,key)
      return root
   
   def min(self,node):
      current=node
      while current.left is not None:
         current=current.left
      return current
   
   def search(self,root,key):
      if root is None:
         return None
      elif root.data == key:
         return root.data
      elif key < root.data:
         return self.search(root.left,key)
      else:
         return self.search(root.right,key)
      
   def delete(self,root,key):
      if root is None:
         return None
      if key < root.data:
         root.left= self.delete(root.left,key)
      elif key > root.data:
         root.right=self.delete(root.right,key)
      else:
         if root.left is None:
            return root.right
         if root.right is None:
            return root.left
         
         temp=self.min(root.right)
         root.data=temp.data
         root.right=self.delete(root.right,temp.data)
      return root
   
   def inorder(self,root):
      if root:
         self.inorder(root.left)
         print(root.data,end=" ")
         self.inorder(root.right)


b=BST()
root=None
datas=[8, 3, 10, 1, 6, 14, 4, 7, 13]
for data in datas:
   root=b.insert(root,data)

b.root=root
print()
b.inorder(b.root)
print()
print(b.min(b.root).data)
b.delete(b.root,3)
print()
b.inorder(b.root)