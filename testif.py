#!/usr/bin/python

aa = input ("A=")
bb = input ("B=")
a=int(aa)
b=int(bb)

if a > b:
   print("A > B")
   print(a - b)

else:
   print("B <= A")
   print(b - a)

print("The End")

def open_file(filename):
   print("Reading file", filename)
   with open(filename) as f:

      return f.read()
      print("Done")

