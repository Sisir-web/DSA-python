import numpy as np
from array import *

# a=(np.array([1,2,3]))
# # print(a)
# # a.count(2)
# # for i in a:
# #    print(i)
# a=np.append(a,33)
# print(a)
# i=0
# while i < len(a):
#    print(f'{i} {a[i]}')
#    i+=1

# a=array('i',[1,2,3,4,5])
# i=0
# for i in range(0,5):
#    print(f'{i} {a[i]}')
# # i=0
# while i<len(a):
#    print(f'{i} {a[i]}')
#    i+=1

a=[]
for i in range(0,5):
   # print("Enter the array elements:")
   value=int(input("Enter the elemtns: "))
   a.append(value)
# print(a)

# sum=sum(a)
# avg=sum/5
# print(f'{sum} and {avg}')
# max=a[0]
# min=a[0]
# for i in a[0:]:
#    print(i)
#    if i<min:
#       min=i
#    if i>max:
#       max=i
# print(min,max)

# arr=[]
# for i in a:
#    arr=[i]+arr
# print(arr)
   
#  Level 2: Searching & Operations
# Check if a given number exists in an array. Print its index if found, otherwise print “Not Found”.
# Count even and odd numbers in an array.
# Remove all occurrences of a given number x from an array.
# Rotate an array to the right by 1 step.
# Example: [1,2,3,4,5] → [5,1,2,3,4]
# Find the second largest number in an array.

# evel 3: Tricky / Common Interview
# Move all zeros to the end of an array while maintaining the order of non-zero elements.
# Example: [0, 1, 0, 3, 12] → [1, 3, 12, 0, 0]
# Find duplicates in an array.
# Example: [1,2,3,2,4,1] → [1,2]
# Merge two sorted arrays into a single sorted array (without using sort() at the end).
# Check if the array is a palindrome
# Example: [1,2,3,2,1] → True
# Find the missing number in an array of size n that contains numbers from 1 to n+1 with one number missing.
# Example: [1,2,4,5] → 3