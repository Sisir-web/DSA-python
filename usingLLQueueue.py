class Node:
   def __init__(self,data=None,next=None):
      self.data=data
      self.next=None

class Queue:
   def __init__(self,head=None):
      self.head=None
   
   def empty(self):
      return self.head is None
   
   def enqueue(self,data):
      new_data=Node(data=data)
      if self.empty():
         self.head=new_data
         return
      new_data.next=self.head
      self.head=new_data
      return
   
   def dequeue(self):
      if self.empty():
         print("Queue is empty")
         return
      if self.head.next is None:
         self.head=None
         return
      current=self.head
      while current.next.next:
         current=current.next
      current.next=None
      return
   
   def front(self):
      if self.empty():
         print("Queue is empty")
         return
      current=self.head
      while current.next:
         current=current.next
      return current.data
   
   def rear(self):
      if self.empty():
         print("Empty Queue")
         return
      return self.head.data
   
   def size(self):
      if self.empty():
         print("Empty Queue")
         return
      count=0
      current=self.head
      while current:
         count+=1
         current=current.next
      return count
   
q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

print(q.front())
print(q.rear())
# q.dequeue()
print(q.front())
print(q.size())
