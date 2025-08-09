class Node:
   def __init__(self,data=None,next=None):
      self.data=data
      self.next=next

class DQLL:
   def __init__(self,head=None,tail=None):
      self.head=None
      self.tail=None

   def empty(self):
      return self.head is None
   
   def enqueufront(self,data):
      new_data=Node(data=data)
      if self.empty():
         self.head=self.tail=new_data
         return
      new_data.next=self.head
      self.head=new_data
      return
   
   def dequeuefront(self):
      if self.empty():
         return
      if self.head==self.tail:
         self.head=None
         return
      self.head=self.head.next
      return
   
   def enqueuerear(self,data):
      new_data=Node(data=data)
      if self.empty():
         self.tail=self.head=new_data
         return
      self.tail.next=new_data
      self.tail=new_data
      return
   
   def dequeuerear(self):
      if self.empty():
         return
      if self.head==self.tail:
         self.head=None
         return
      current=self.head
      while current.next != self.tail:
         current=current.next
      current.next=None
      self.tail=current
      return
      
   def rear(self):
      if self.empty():
         return
      else:
         return self.tail.data
      
   def front(self):
      if self.empty():
         return
      else:
         return self.head.data
      
   def size(self):
      if self.empty():
         return
      current=self.head
      count=0
      while current:
         count+=1
         current=current.next
      return count
   
   def traverse(self):
      if self.empty():
         return
      current=self.head
      print("None->",end="")
      while current:
         print(current.data,end="->")
         current=current.next
      print("None")
      return
      
   
dq=DQLL()

dq.enqueufront(2)
dq.enqueufront(3)
dq.enqueuerear(1)
dq.enqueuerear(0)

# dq.dequeuefront()
# dq.dequeuerear()

print(dq.front())
print(dq.rear())
print(dq.size())
dq.traverse()

      


