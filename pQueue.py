class Node:
   def __init__(self,data=None,priority=None):
      self.data=data
      self.priority=priority

class priorityqueue:
   def __init__(self):
      self.list=[]

   def empty(self):
      return len(self.list) == 0
   
   def push(self,data,priority):
      new_data=(data,priority)
      if self.empty():
         self.list.append(new_data)
         return
      index=0
      while index < len(self.list) and self.list[index][1]<=priority:
         index+=1
      # index=new_data
      self.list.insert(index,new_data)
      return
   
   def pop(self):
      if self.empty():
         raise IndexError("Empty Priority Queue")
      self.list.pop(0)[0]
      return
   
   def size(self):
      if self.empty():
         raise IndexError("empty priority Queue")
      return len(self.list)
   
   def peek(self):
      if self.empty():
         raise IndexError("Queue is Empty")
      return self.list[0]
   
   def traverse(self):
    if self.empty():
        raise IndexError("Empty queue")
    for data, priority in self.list:
        print(f"{data}({priority})", end=" - ")
    print("None")


pq=priorityqueue()
# print(pq.empty())
pq.push(5,1)
pq.push(6,2)
pq.push(3,5)
pq.push(8,9)
pq.push(10,12)
pq.pop()
# print(pq.peek())
print(pq.traverse())


# class Node:
#     def __init__(self, data, priority):
#         self.data = data
#         self.priority = priority

# class PriorityQueueList:
#     def __init__(self):
#         self.list = []

#     def empty(self):
#         return len(self.list) == 0

#     def push(self, data, priority):
#         new_data = (data, priority)

#         # If empty, just append
#         if self.empty():
#             self.list.append(new_data)
#             return

#         # Find the right index to insert (sorted by priority: lower number = higher priority)
#         index = 0
#         while index < len(self.list) and self.list[index][1] <= priority:
#             index += 1

#         # Insert at the found index
#         self.list.insert(index, new_data)

#     def pop(self):
#         if self.empty():
#             raise Exception("Priority Queue is empty")
#         return self.list.pop(0)  # Remove the highest priority item

#     def peek(self):
#         if self.empty():
#             raise Exception("Priority Queue is empty")
#         return self.list[0]

#     def display(self):
#         print("Queue:", self.list)


# # Example
# pq = PriorityQueueList()
# pq.push("task1", 3)
# pq.push("task2", 1)
# pq.push("task3", 2)

# pq.display()
# print("Pop:", pq.pop())
# pq.display()
