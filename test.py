a = 10
b = 6

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

