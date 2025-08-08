class Node:
   def __init__(self,data=None,next=None):
      self.data=data
      self.next=None

class SLL:
   def __init__(self,head=None):
      self.head=head

   def empty(self):
       return self.head is None
       
   
   def insert_at_first(self,data):
      new_node=Node(data=data)
      if self.empty():
         self.head=new_node
         return
      new_node.next=self.head
      self.head=new_node

   def delete_at_last(self):
      if self.empty():
         print("Empty")
         return
      if self.head.next is None:
         self.head=None
         return
      current=self.head
      while current.next.next:
         current=current.next
      if current.next:
         current.next=None
         
   
   def traverse(self):
      if self.empty():
         return
      current=self.head
      while current:
         print(current.data,end="->")
         current=current.next
      print("None")

   def size(self):
      if self.empty():
         return
      total=0
      current=self.head
      while current:
         total +=1
         current=current.next
      return total
   
   def front(self):
      if self.empty():
         return
      current=self.head
      while current.next:
         current=current.next
      return current.data

   def rear(self):
      if self.empty():
         return
      return self.head.data
 
# s=SLL()
# # print("empty",s.empty())
# s.insert_at_first(3)
# s.insert_at_first(1)
# s.insert_at_first(4)

# print(s.traverse())
# print(s.size())
# print("delete position: ",s.front())
# print('insert position: ',s.rear())
# # print("Now not empty",s.empty())
# # s.delete_at_last()
# # print(s.traverse())

class Queue(SLL):

   def is_empty(self):
     return self.empty()
   
   def enqueue(self,data):
      return self.insert_at_first(data)
      
   def dequeue(self):
      return self.delete_at_last()
   
   def insertposition(self):
      return self.rear()
      
   def deleteposition(self):
      return self.front()
      
   def qsize(self):
      return self.size()

Q=Queue()
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.enqueue(4)
print(Q.insertposition())
print(Q.deleteposition())
print(Q.size())
Q.dequeue()
print(Q.deleteposition())
