class Node:
   def __init__(self,data=None,next=None):
      self.data=data
      self.next=next

class Linked_List:
   def __init__(self,head=None):
      self.head=head

   def is_empty(self):
      return self.head == 0
   
   def insert(self,data):
      new_node=Node(data)
      # if self.is_empty():
      #    new_node.next=self.head
      #    self.head.next=new_node
      #    self.head=new_node
      #    return
      new_node.next=self.head
      self.head=new_node

   def delete(self):
      if self.is_empty():
         print("Empty stack")
      if self.head.next == None:
         self.head=None
         return
      self.head=self.head.next
      return
   
   def traverse(self):
      if self.is_empty():
         return None
      current=self.head
      while current:
         print(current.data,end="->")
         current=current.next
      print("None")
   
# L=Linked_List()
# L.insert(2)
# L.insert(3)
# L.insert(4)
# L.traverse()
# L.delete()
# L.traverse()
class stack(Linked_List):

   def push(self,data):
      self.insert(data)

   def pop(self):
      if self.is_empty():
         print("stacck is empty")
      self.delete()

   def peek(self):
      
      return None if self.is_empty() else self.head.data
      
   # def size(self):
   #    return len(self.Linked_List)
   
s=stack()
s.push(2)
s.push(1)
s.push(3)
s.push(5)
s.pop()
print(s.peek())
# s.size()
      
# | Approach                      | Type           | Inheritance? | Pros                 | Cons                           |
# | ----------------------------- | -------------- | ------------ | -------------------- | ------------------------------ |
# | Python `list`                 | Built-in       | No           | Fast, simple         | No control/custom logic        |
# | Extend `list`                 | Built-in + OOP | Yes          | Clean interface      | Still depends on Python `list` |
# | Manual Singly Linked List     | Custom         | No           | Full control         | More code to manage            |
# | Extend Singly Linked List     | Custom + OOP   | Yes          | Code reuse + clarity | Inheritance can be limiting    |
# | Use Linked List (composition) | Custom + Clean | No           | Most flexible design | Slightly more boilerplate      |

   