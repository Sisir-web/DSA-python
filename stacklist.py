# class stack:
#    def __init__(self):
#       self.list=[]

#    def is_empty(self):
#          return len(self.list) == 0
   
#    def push(self,data):
#        self.list.append(data)
     
   
#    def pop(self):
#       if not self.is_empty():
#          return self.list.pop()
#       else:
#          print("stack is empty")
      
#    def peek(self):
#       if not self.is_empty():
#          return self.list[-1]
#       else:
#          print("Empty stack No peek")
      
#    def size(self):
#       return len(self.list)
   
# s=stack()
# s.push('a')
# s.push('b')
# s.push('c')
# # s.pop()
# # s.pop()
# print("This is the top item in stack",s.peek())
# print("The size of the stack ",s.size())
      


















class stack:
   def __init__(self):
      self.list=[]

   def is_empty(self):
      return len(self.list) == 0
   
   def push(self,data):
      return self.list.append(data)
   
   def pop(self):
      if not self.is_empty():
         return self.list.pop()
      else:
         return "empty"
      
   def peek(self):
      if not self.is_empty():
         return self.list[-1]
      else:
         print("Empty stack")

   def size(self):
      if not self.is_empty():
         return len(self.list)
      
s=stack()
s.push(3)
s.push(4)
s.push(2)
s.push(1)

s.pop()
print(s.peek())
print(s.size())