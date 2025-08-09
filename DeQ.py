#1. Using List.
# class DQ:
#    def __init__(self):
#       self.list=[]

#    def is_empty(self):
#       if len(self.list) == 0:
#          print("Dequeue is empty")
#          return

#    def insert_at_front(self,data):
#       front=self.list.insert(0,data)
#       print(f'Inserted value at front: {data}')
#       return

#    def delete_at_front(self):
#       if not self.is_empty():
#          return self.list.pop(0)
#       else:
#          print("Queue is Empty")
#          return 
      
#    def insert_at_last(self,data):
#       last=self.list.append(data)
#       print(f'Last position Insertion data: {data}')
#       return

#    def delete_at_last(self):
#       if not self.is_empty():
#          return self.list.pop(-1)
#       else:
#          print("Dequeue is empty can't delete")
#          return

#    def get_front(self):
#       if not self.is_empty():
#          return self.list[0]
#       else:
#          print("Empty Dequeue")
#          return

#    def get_last(self):
#       if not self.is_empty():
#          return self.list[-1]
#       else:
#          print("Dequeue is Empty")
#          return

#    def size(self):
#       if not self.is_empty():
#          return len(self.list)
#       else:
#          print('Dequeue is Empty')
#          return

# dq=DQ()
# dq.insert_at_front(1)
# dq.insert_at_front(2)
# dq.insert_at_front(3)
# dq.insert_at_front(4)
# dq.insert_at_last(9)
# dq.insert_at_last(10)

# print('Here we didnt deleted from 0th: ',dq.get_front())
# print('Here we deleted from the last -1th: ',dq.get_last())
# print(dq.size())

# dq.delete_at_front()
# dq.delete_at_last()
# print('Deleted the front value 0th (4) index: ',dq.get_front())
# print('Deleted the last value -1th (10) index: ',dq.get_last())

#By extending list class......
# class DQ(list):
#    # def __init__(self):
#    #    self.list=[]

#    def is_empty(self):
#       if len(self) == 0:
#          print("Dequeue is empty")
#          return

#    def insert_at_front(self,data):
#       front=self.insert(0,data)
#       print(f'Inserted value at front: {data}')
#       return

#    def delete_at_front(self):
#       if not self.is_empty():
#          return self.pop(0)
#       else:
#          print("Queue is Empty")
#          return 
      
#    def insert_at_last(self,data):
#       last=self.append(data)
#       print(f'Last position Insertion data: {data}')
#       return

#    def delete_at_last(self):
#       if not self.is_empty():
#          return self.pop(-1)
#       else:
#          print("Dequeue is empty can't delete")
#          return

#    def get_front(self):
#       if not self.is_empty():
#          return self[0]
#       else:
#          print("Empty Dequeue")
#          return

#    def get_last(self):
#       if not self.is_empty():
#          return self[-1]
#       else:
#          print("Dequeue is Empty")
#          return

#    def size(self):
#       if not self.is_empty():
#          return len(self)
#       else:
#          print('Dequeue is Empty')
#          return

# dq=DQ()
# dq.insert_at_front(1)
# dq.insert_at_front(2)
# dq.insert_at_front(3)
# dq.insert_at_front(4)
# dq.insert_at_last(9)
# dq.insert_at_last(10)

# print('Here we didnt deleted from 0th: ',dq.get_front())
# print('Here we deleted from the last -1th: ',dq.get_last())
# print(dq.size())

# dq.delete_at_front()
# dq.delete_at_last()
# print('Deleted the front value 0th (4) index: ',dq.get_front())
# print('Deleted the last value -1th (10) index: ',dq.get_last())

#Using double linked list class....
class Node:
   def __init__(self,data=None,next=None,prev=None):
      self.data=data
      self.next=None
      self.prev=None

class DLLQ:
   def __init__(self,head=None,tail=None):
      self.head=None
      self.tail=None

   def empty(self):
      return self.head is None
   
   def insert_at_front(self,data):
      new_data=Node(data=data)
      if self.empty():
         self.head=self.tail=new_data
         return
      new_data.next=self.head
      self.head.prev=new_data
      self.head=new_data

   def delete_at_front(self):
      if self.empty():
         return
      if self.head==self.tail: #one node condition
         self.head=self.tail=None
         # self.head.prev=None
         return
      self.head=self.head.next
      self.head.prev=None
      return
      
   def insert_at_rear(self,data):
      new_data=Node(data=data)
      if self.empty():
         self.tail=self.head=new_data
         return
      new_data.prev=self.tail
      self.tail.next=new_data
      self.tail=new_data
      return
      
   def delete_at_rear(self):
      if self.empty():
         return
      if self.tail.prev==self.head:
         self.tail=self.head=None
         return    
      self.tail=self.tail.prev
      self.tail.next=None
      return
   
   def traversefront(self):
      if self.empty():
         return
      current=self.head   
      print("None<->",end="")
      while current:
         print(current.data,end="<-->")
         current=current.next
      print("None")
      return
   
   # def traverserear(self): #don't need this 
   #    if self.empty():
   #       return
   #    last=self.tail
   #    while last:
   #       print(last.data,end="<->")
   #       last=last.prev
   #    print()
   #    return

   def get_front(self):
      if self.empty():
         return 
      else:
         return self.head.data
      
   def get_rear(self):
      if self.empty():
         return
      else:
         return self.tail.data
      
   def size(self):
      if self.empty():
         return
      current=self.head
      count=0
      while current:
         count+=1
         current=current.next
      return count
   
Dq=DLLQ()
Dq.insert_at_front(1)
Dq.insert_at_front(2)
Dq.insert_at_front(3)
Dq.insert_at_rear(9)
Dq.insert_at_rear(8)
Dq.insert_at_rear(7)
Dq.delete_at_front()
Dq.delete_at_rear()
print(Dq.traversefront())
print(Dq.get_front())
print(Dq.get_rear())
print(Dq.size())
