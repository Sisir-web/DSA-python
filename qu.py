# class q:
#    def __init__(self):
#       self.queu=[]

#    def empty(self):
#       return len(self.queu) == 0
   
#    def enque(self,data):
#       inserted = self.queu.append(data)
#       print(f'Inserted data = {data}')
#       return inserted

#    def deque(self):
#       if not self.empty():
#          deleted = self.queu.pop(0)
#          print(f'Deleted = {deleted}')
#          return deleted
#       else:
#          print(f'Empty Queue')

#    def rear(self):
#       if not self.empty():
#          rear = self.queu[-1]
#          print(f'Rear={rear}')
#          return rear
#       else:
#          print('Queue is Empty')
   
#    def front(self):
#       if not self.empty():
#          front = self.queu[0]
#          print(f'Front = {front}')
#          return front
#       else:
#          print("queue Empty")

#    def size(self):
#       if not self.empty():
#          size =len(self.queu)
#          return size
#       else:
#          print('empty queue')


# Q = q()
# # print(Q.empty())
# Q.enque(1)
# Q.enque(2)
# Q.enque(3)
# Q.enque(4)
# print(Q.front())
# print(Q.rear())
# Q.deque()
# print(Q.front())

class Queue(list):

   def empty(self):
      return len(self) == 0
   
   def enqueue(self,data):
      return self.append(data)
   
   def dequeue(self):
      if not self.empty():
         return self.pop(0)
      
   def front(self):
      if not self.empty():
         return self[0]
      
   def rear(self):
      if not self.empty():
         return self[-1]
      
   def size(self):
      if not self.empty():
         return len(self)

s=Queue()
s.enqueue(2)
s.enqueue(1)
s.enqueue(5)
print("size of queue",s.size())
print("The front delete value",s.front())
print("The insert position value",s.rear())