#Question 1 print all natural number in reverse and normal way
# class R:
#    def func(self,n):
#       if n==0:
#          return 
#       else:
#           print(n ,end="<-->")
#           self.func(n-1)
          
# r=R()
# r.func(100)

# #Question 2  write a recursive function to print all the N odd natural numbers also print in reverse order and do for the even too
# class R:
#    def func(self,n):
#       if n==0 :
#          return
#       else:
#          if n%2==0:      #reverse order
#             print(n)
         
#          self.func(n-1)
# #          # if n%2!=0:          #ascending order
# #          #      print("odd :",n)
# #          # else:
# #          #    return
# r=R()
# r.func(10)


#Question 3 
# class R:
#    def func(self,n):
#       if n==1:
#          return 1
#       elif n%2 != 0: 
#             return n + self.func(n-1)
#       else:
#           return self.func(n-1)
                  
# r=R()
# s=r.func(9)
# print(s)
#Sum of first 10 natural even numbers...
# class R:
#    def func(self, n):
#       if n==1:
#          return 2
#       else:
#          return (2*n)+ self.func(n-1)
# r=R()
# s=r.func(10)
# print(s)
#sum of first n natural 10 odd numbers 
# class R:
#    def func(self,n):
#       if n==1:
#          return 1
#       else:
#          return (2*n-1)+self.func(n-1)
      
# r=R()
# s=r.func(10)
# print(s)
#Find the factorial of a number
# class R:
#    def func(self,n):
#       if n==1:
#          return 1
#       else:
#          return n*self.func(n-1)
# r=R()
# print(r.func(5))

#Sum of square of first N natural numbers
class R:
   def func(self,n):
      if n==1:
         return 1
      else:
         return (n*n)+self.func(n-1)

r=R()
print(r.func(6))
      



