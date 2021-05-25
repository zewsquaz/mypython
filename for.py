#!/usr/bin/python


# My new changes 


hugehairypants = [ "big", "wors", "shorts" ]

for i in hugehairypants:
   print(i)
   for j in hugehairypants:
      print(j)


for x in range(0, 5):
    print('Hello  %s' % x)


for i in range(10, 0, -1): print(i)

mlist =  range(10, 0, -1)

print mlist


print (" \n len(mlist)= %s \n" % len(mlist)   )

s =""
for i in range(1,4):
    s=s+"   " + str(i).rjust(3)
s = "   "+s
print s
print

tabu=[ ]  
row=[]


for i in range(1,4):
    s=str(i).ljust(3) + "   "
    for k in range(1,4):
        s = s + str(i*k).rjust(3)+ "   "
        row.append( i*k) 
    tabu.append(row)
    row=[]
    print s    


print tabu





