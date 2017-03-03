#! /usr/bin/python

#A = [37, 12, 89, 90, 2, 3, 1, 45]
print "Insertion Sort"
option = raw_input("Please select the type of input 1.Integer 2.String:")
string_input = raw_input("Enter list of elements seperated by space to sort:")
A = string_input.split()

if option == "1":
  A= [int(a) for a in A]
print "Unsorted list:"
print A

i = 1

for item in A:
  if A.index(item) == i:
    key = A[i]
    j = i - 1
    while j >= 0 and A[j] > 0 and A[j] > key:
      A[j+1] = A[j]
      j = j - 1
    A[j+1] = key
    i = i + 1

print "Sorted list:"
print A 
