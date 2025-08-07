# class node:
#    def __init__(self,item=None,next=None):
#       self.item=item
#       self.next=next

# class S:
#    def __init__(self):
#       self.head=None

#    def is_empty(self):
#       if self.head is None:
#          return self.head is None
      
#    def traverse(self):
#       if self.is_empty():
#          print("Linkedlist is empty")
#          return
#       start=self.head
#       while start:
#          print(start.item, end="->")
#          start=start.next
#       print("None")

#    def at_begining(self,item):
#       new_node=node(item)
#       new_node.next=self.head
#       self.head=new_node

#    def at_end(self,item):
#       new_node=node(item)
#       if self.is_empty():
#          self.head = new_node
#          return
#       current=self.head
#       while current.next:
#          current=current.next
#       current.next=new_node

#    def after_value(self,key,item):
#       current=self.head
#       while current and current.next.item != key:
#          current=current.next
#       if not current:
#          print(f'{key} is not avaiable')
#       new_node=node(item)
#       new_node.next=current.next
#       current.next=new_node

#    def delete_by_value(self,data):
#       if self.is_empty():
#          print("List is empty")
#          return
      
#       if self.head.data==data: #special scenario where the the head is the data to be deleted
#          self.head=self.head.next #move the old head to the next head old one auto deleted as garbage value
#          return
      
#       current=self.head
#       while current.next and current.next.data != data: #Traverse the node untill the data is there
#          current=current.next
#       if current.next:
#          current.next=current.next.next #IF the node was found bypass it.
#       else:
#          print(f'{data} not found in the list')

#    def delete_begining(self,data):
#       if self.is_empty():
#          print("Empty")
#          return
#       self.head=self.head.next

#    def delete_end(self,data):
#       if self.is_empty():
#          print("Empty")
#          return
#       if self.head is None: #Special case where only 1 value is there
#          self.head=None #deleting the last make it None
#          return
#       current=self.head
#       while current.next.next: #while current.next -> stop at last node while current.next.next second last
#          current=current.next
#          current.next=None


# # ----------------- Testing -----------------
# ll = S()

# # Insertions
# ll.at_end(10)
# ll.at_end(20)
# ll.at_end(30)
# ll.at_beginning(5)
# ll.after(20, 25)

# print("Traverse after insertions:")
# ll.traverse()

# # Deletions
# ll.delete_by_value(25)
# ll.delete_beginning()
# ll.delete_end()

# print("Traverse after deletions:")
# ll.traverse()

# print("Is Empty?:", ll.is_empty())
      


   
class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class S:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def traverse(self):
        if self.is_empty():
            print("Linkedlist is empty")
            return
        start = self.head
        while start:
            print(start.item, end=" -> ")
            start = start.next
        print("None")

    def at_beginning(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def at_end(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def after_value(self, key, item):
        current = self.head
        while current and current.item != key:
            current = current.next
        if not current:
            print(f'{key} is not available')
            return
        new_node = Node(item)
        new_node.next = current.next
        current.next = new_node

    def delete_by_value(self, data):
        if self.is_empty():
            print("List is empty")
            return
        
        if self.head.item == data:  # delete head
            self.head = self.head.next
            return
        
        current = self.head
        while current.next and current.next.item != data:
            current = current.next
        
        if current.next:
            current.next = current.next.next
        else:
            print(f'{data} not found in the list')

    def delete_beginning(self):
        if self.is_empty():
            print("Empty")
            return
        self.head = self.head.next

    def delete_end(self):
        if self.is_empty():
            print("Empty")
            return
        if self.head.next is None:  # only one node
            self.head = None
            return
        current = self.head
        while current.next.next:  # stop at second last
            current = current.next
        current.next = None

# ----------------- Testing -----------------
ll = S()

# Insertions
ll.at_end(10)
ll.at_end(20)
ll.at_end(30)
ll.at_beginning(5)
ll.after_value(20, 25)

print("Traverse after insertions:")
ll.traverse()

# Deletions
ll.delete_by_value(25)
ll.delete_beginning()
ll.delete_end()

print("Traverse after deletions:")
ll.traverse()

print("Is Empty?:", ll.is_empty())

