class Node:
   def __init__(self,prev=None,data=None,next=None):
      self.prev=prev
      self.data=data
      self.next=next

class DLL:
   def __init__(self,head=None):
      self.head=head

   def is_empty(self):
         return self.head is None
   
   def insert_at_first(self,data):
      new_node=Node(data=data)
      if self.is_empty():
         self.head=new_node
      else:  
         new_node.next=self.head
         self.head=new_node
         new_node.prev=None

   def insert_at_end(self,data):
      new_node=Node(data=data)
      if self.is_empty():
         self.head=new_node
         return
      current=self.head
      while current.next:
         current=current.next
      current.next=new_node
      # new_node=current
      new_node.next=None
      new_node.prev=current.next

   def insert_by_value(self,key,data):
      new_node=Node(data=data)
      if self.is_empty():
         self.head=new_node
         return
      current=self.head
      while current and current.data != key:
         current=current.next
      if current is None:
         print(f'{key} not found')
         return
      next_node=current.next #save the original link before linking new one as next
      current.next=new_node
      new_node.next=next_node
      new_node.prev=current

   def traverse(self):
      if self.is_empty():
         print("0 items in DLL")
      current=self.head
      while current:
         print(current.data ,end="<->")
         current=current.next
      print("none")

   def delete_at_first(self):
      if self.is_empty():
         print('empty list')
         return 
      if self.head.next is None:
         self.head=None
         return
      self.head=self.head.next
      self.head.prev=None    

   def delete_at_end(self):
      if self.is_empty():
         print("Empty delete function")
      try:
         if self.head.next is None:
            self.head = None
            return
         current=self.head
         while current and current.next.next:
            current=current.next
         current.next=None
         current.prev=current
      except:
         print("No head today sorry babe :( ")

   def delete_by_value(self,key):
      if self.is_empty():
         print("List is empty")
         return
      if self.head == key:
         self.head=self.head.next
         return
      current=self.head
      while current.next and current.next.data != key:
         current=current.next
      if current.next:
         current.next=current.next.next
         current.prev=current.next
      else:
         print(f'{key} not found')
         return 
      
   def search(self,key):
      if self.is_empty():
         print("Empty List")
         return
      if self.head.data == key:
         return self.head.data
      
      current=self.head
      while current.next and current.next.data != key:
         current=current.next
      if current.next:
         return current.next.data
      else:
         print(f'{key} is not there in list')

d=DLL()
d.insert_at_first(1)
d.insert_at_first(2)
d.insert_at_first(3)
d.insert_at_first(4)
d.insert_at_first(5)
# d.insert_by_value(1,11)
# d.insert_by_value(11,12)
# d.insert_at_end(0)
# d.insert_at_end(33)

d.traverse()
# d.delete_at_first()
# print("after deleting the first index data")
# d.traverse()
# d.delete_at_end()
# print("after deleteing the last index data")
# d.traverse()
# print('if it is empty show: ', d.is_empty())
# d.traverse()
# d.delete_at_end()
d.delete_by_value(4)
d.traverse()
print(d.search(5))
d.search(9)