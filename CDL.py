class Node:
   def __init__(self,prev=None,data=None,next=None):
      self.data=data
      self.next=next
      self.prev=prev

class CDL:
   def __init__(self,head=None):
      self.head=head

   def is_empty(self):
      return self.head is None
   
   def traverse(self):
      if self.is_empty():
         print("Empty list")
         return
      current=self.head
      while current:
         print(current.data,end="<-->")
         current=current.next
         if current==self.head:
            break
      print(f'back to first node-->{self.head.data}')

   def insert_at_first(self,data):
      new_node=Node(data=data)

      if self.head is None:   
         new_node.next=new_node
         new_node.prev=new_node 
         self.head=new_node
         return
      
      last_node=self.head.prev #this is the last node in CDLL

      new_node.next=self.head
      new_node.prev=last_node

      last_node.next=new_node
      self.head.prev=new_node

      self.head=new_node
   
   def insert_by_value(self,key,data):
      new_node=Node(data=data)
      if self.is_empty():
         new_node.next=new_node
         new_node.prev=new_node
         self.head=new_node
         return
      
      current=self.head
      while True:
         if current.data == key:
            next_node=current.next

            current.next=new_node
            new_node.prev=current
            new_node.next=next_node
            next_node.prev=new_node
            return
         current=current.next
         
         if current==self.head:
            print(f'{key} not found')
            return
   
   def insert_at_end(self,data):
      new_node=Node(data=data)
      if self.is_empty():
         self.head=new_node
         new_node.next=self.head
         new_node.prev=self.head
         return
      current = self.head
      while current.next != self.head:
            current=current.next
      current.next=new_node
      new_node.next=self.head
      self.head.prev=new_node
      new_node.prev=current

   def delete_at_first(self):
      if self.is_empty():
         return
      if self.head.next == self.head:
          self.head = None
          return
      last_node=self.head.prev
      new_head=self.head.next
      last_node.next=new_head
      last_node.prev=new_head
      new_head.prev=last_node
      self.head=new_head
      
   def delete_b_value(self,key):
      if self.is_empty():
         return 
      if self.head.data == key and self.head.next == self.head:
         self.head=None
         return
      current=self.head
      while current.next != self.head and current.next.data != key:
         current=current.next
      
      if current.next==self.head:
         print(f"{key} is not available")
         return
      else:
         current.next=current.next.next
         current.prev=current
         return
      
   def delete_at_end(self):
      if self.is_empty():
         return
      if self.head.next == self.head:
         self.head=None
         return
      current=self.head
      while current.next.next != self.head:
         current=current.next
      current.next=self.head   
      self.head.prev=current
      return
   
   def search(self,key):
      if self.is_empty():
         return
      current=self.head
      while current.next != self.head and current.next.data != key:
         current=current.next
      if current.next.data == key:
         print(f"{key} is available")
      else:
         print(f'{key } is not avaiable')

         
     


   
cd=CDL()

cd.insert_at_first(0) 
cd.insert_at_first(1) 
cd.insert_at_first(2)
cd.insert_at_first(3)
# cd.insert_at_first(5)
# cd.insert_at_first(4)
cd.traverse()
# cd.insert_at_end(44)
# cd.traverse()
# cd.insert_at_end(55)
# cd.traverse()
# cd.delete_at_first()
# cd.traverse()
cd.delete_b_value(8)
cd.traverse()
cd.delete_at_end()
cd.traverse()
cd.search(99)

# cd.insert_by_value(3,11)
# cd.traverse()
# cd.insert_by_value(6,19)
