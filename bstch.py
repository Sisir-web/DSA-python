class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    # Insert a node into BST
    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.data:
            root.left = self.insert(root.left, key)
        elif key > root.data:
            root.right = self.insert(root.right, key)
        return root

    # Search for a key in BST
    def search(self, root, key):
        if root is None:
            return None
        elif root.data == key:
            return root.data  # ✅ Return the data instead of the node
        elif key < root.data:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    # Inorder traversal (sorted order)
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    # Find the node with the smallest value in a tree
    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Delete a node from BST
    def delete(self, root, key):
        if root is None:
            return root

        # Search for the node to delete
        if key < root.data:
            root.left = self.delete(root.left, key)
        elif key > root.data:
            root.right = self.delete(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children
            temp = self.minValueNode(root.right)  # ✅ Find smallest in right subtree
            root.data = temp.data  # ✅ Copy smallest value to current node
            root.right = self.delete(root.right, temp.data)  # ✅ Delete duplicate in right subtree

        return root


# --- Test the BST ---
tree = BST()
root = None
keys = [8, 3, 10, 1, 6, 14, 4, 7, 13]

for key in keys:
    root = tree.insert(root, key)

print("Inorder Traversal (Sorted):")
tree.inorder(root)

# Search
print("\nSearch result:", tree.search(root, 7))

# Delete
root = tree.delete(root, 3)
print("Inorder after deleting 3:")
tree.inorder(root)
