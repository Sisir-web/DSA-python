# class Node:
#    def __init__(self,left=None,data=None,right=None):
#       self.data=data
#       self.left=left
#       self.right=right

# class BST:
#    def __init__(self):
#       self.root=None


#    def empty(self):
#       return self.root is None
   
#    def insert(self,root,data):
#       if self.root is None:
#          return Node(data)
      
#       if data < root.data:
#          root.left=self.insert(root.left,data)
#       elif data > root.data:
#          root.right=self.insert(root.right,data)
#       return root
   
#    def inorder(self,root):
#       if root:
#          self.inorder(root.left)
#          print(root.data,end=" ")
#          self.inorder(root.right)

# bs=BST()
# root=None
# for value in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
#    root=bs.insert(root,value)
# print(bs.empty())
       
# print("Inorder Traversal (Sorted):")
# bs.inorder(bs.root)

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def empty(self):
        return self.root is None

    def insert(self, root, data):
        if root is None:  # check for local root
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def search(self,root,key):
        if root is None:
            return
        elif root.data == key :
            return key
        if root.left.data == key:
            return key
        elif root.right.data == key:
            return key
        else:
            print(f"{key} is not available in this tree")

# Create tree
bs = BST()
for value in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
    bs.root = bs.insert(bs.root, value)  # Assign to bs.root

# Check if empty
print(bs.empty())  # Should print False

# Print inorder traversal
print("Inorder Traversal (Sorted):")
bs.inorder(bs.root)
print()
print("The search opt: ")
print(bs.search(bs.root,17))
