class Node:
   def __init__(self,data=None,next=None):
      self.data=data
      self.next=next

class CSL:
   def __init__(self,head=None):
      self.head=head

   def is_empty(self):
      if self.head is None:
         return self.head is None
      
   def insert_at_first(self, data):
      new_node = Node(data)
      if self.is_empty():
         self.head = new_node
         new_node.next = self.head
         return
      current = self.head
      while current.next != self.head:
         current = current.next
      new_node.next = self.head
      self.head = new_node
      current.next = self.head  # make it circular


   def insert_by_value(self,key,data):
      new_node=Node(data=data)
      if self.head and self.head.data== key:
         self.head.next=new_node
         return
      try:
         current=self.head
         while current and current.data != key:
            current=current.next
         if current:
            new_node.next=current.next
            current.next=new_node
         else:
            print(f"{key} not found")
      except:
         print("")

   def insert_at_end(self,data):
      new_node = Node(data=data)
      if self.is_empty():
         self.head=new_node
         return
      current=self.head
      while current.next:
         current=current.next
      new_node.next=current.next
      current.next=new_node
      

   def traverse(self):
      if self.is_empty():
         print("Empty xa hai")
         return
      current=self.head
      while current:
         print(current.data , end="->")
         current=current.next
         if current == self.head:
            break
      print(f"first node ->{self.head.data}")

   def delete_first(self):
      if self.is_empty():
         return
      if self.head:
         self.head=self.head.next
         return
      
   def delete_value(self,key):
      if self.is_empty():
         return
      if self.head == key:
         self.head=None
         return
      current=self.head
      while current.next and current.next.data != key:
         current=current.next
      if not current.next:
         print(f'{key} not found')
      else:
         current.next=current.next.next

   def delete_at_end(self):
      if self.is_empty():
         return
      if self.head.next is None:
         self.head = None
         return 
      current=self.head
      while current.next and current.next.next:
         current=current.next
      current.next=None
   
cs=CSL()

cs.is_empty()
cs.insert_at_first(33)
cs.insert_at_first(30)
cs.insert_at_first(31)
cs.insert_by_value(31,2)
cs.insert_by_value(36,2)
cs.insert_at_end(40)
cs.insert_at_end(700)
cs.insert_at_end(60)

cs.traverse()

# cs.delete_first()
# cs.traverse()
      
# cs.delete_first()
# cs.traverse()

# cs.delete_first()
# cs.traverse()
# cs.delete_value(33)
# cs.traverse()
cs.delete_at_end()
cs.traverse()