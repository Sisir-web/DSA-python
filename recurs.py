class R:
   # def __init__(self):
   #    self.n=None
   
   def func(self,n):
      if n==1:
         return 1
      else:
         return n + self.func(n-1)
      
r=R()
result=r.func(100)
print(result)