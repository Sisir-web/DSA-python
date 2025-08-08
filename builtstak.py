# class Node:
#    def __init__(self,data=None):
#       self.data=data
#       self.next=None

# class stack:
#    def __init__(self,head=None):
#       self.head=head

#    def is_empty(self):
#       print("Stack is Empty")
#       return self.head is None
      
#    def push(self,data):
#       new_node=Node(data)
#       if self.is_empty():
#          new_node.next=self.head
#          self.head=new_node 
#          return
#       new_node.next=self.head
#       self.head=new_node

#    def pop(self):
#       if self.is_empty():
#          return
#       if self.head.next is None:
#          self.head=None
#          return 
#       self.head=self.head.next

#    def peek(self):
#       return self.head.data if not self.is_empty() else None

# s=stack()
# s.is_empty()
# # s.push(4)
# # s.push(45)
# # s.push(455)
# # s.pop()
# # print(s.peek())
      
class stack:
   def __init__(self):
      self.list=[]

   def empty(self):
       return len(self.list)==0
   
   def push(self,data):
         
         self.list.append(data)
         return
   
   def pop(self):
      if not self.empty():
         return self.list.pop()
      else:
         print("Empty stack")
      
      
   def peek(self):
      if not self.empty():
         return self.list[-1]
      else:
         return "empty"
   
   def size(self):
      return len(self.list)
   
s=stack()
s.push(5)
s.push(3)
s.push(1)
s.pop()
print(s.peek())
print(s.size())
      
                                                      


# cd C:\Users\sisir\OneDrive\Desktop\DSAPython

# # Stage your changes (add new or modified files)
# git add .

# # Commit with a meaningful message (e.g., based on topic or problem)
# git commit -m "Solved problems on stacks and queues - Day 5"

# # Push to GitHub
# git push origin main
