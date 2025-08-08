#1. Using List.
class DQ:
   def __init__(self):
      self.list=[]

   def is_empty(self):
      if len(self.list) == 0:
         print("Dequeue is empty")
         return

   def insert_at_front(self,data):
      front=self.list.insert(0,data)
      print(f'Inserted value at front: {data}')
      return

   def delete_at_front(self):
      if not self.is_empty():
         return self.list.pop(0)
      else:
         print("Queue is Empty")
         return 
      
   def insert_at_last(self,data):
      last=self.list.append(data)
      print(f'Last position Insertion data: {data}')
      return

   def delete_at_last(self):
      if not self.is_empty():
         return self.list.pop(-1)
      else:
         print("Dequeue is empty can't delete")
         return

   def get_front(self):
      if not self.is_empty():
         return self.list[0]
      else:
         print("Empty Dequeue")
         return

   def get_last(self):
      if not self.is_empty():
         return self.list[-1]
      else:
         print("Dequeue is Empty")
         return

   def size(self):
      if not self.is_empty():
         return len(self.list)
      else:
         print('Dequeue is Empty')
         return

dq=DQ()
dq.insert_at_front(1)
dq.insert_at_front(2)
dq.insert_at_front(3)
dq.insert_at_front(4)
dq.insert_at_last(9)
dq.insert_at_last(10)

print('Here we didnt deleted from 0th: ',dq.get_front())
print('Here we deleted from the last -1th: ',dq.get_last())
print(dq.size())

dq.delete_at_front()
dq.delete_at_last()
print('Deleted the front value 0th (4) index: ',dq.get_front())
print('Deleted the last value -1th (10) index: ',dq.get_last())
