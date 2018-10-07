b = input("Enter a number with 4-digits: ")

a = str(b)
b = a[0]
z = int(a[0])
c = a[1]
v = int(a[1])
e = a[2]
y = int(a[2])
m = a[3]
h = int(a[3])

f = z * v * y * h

x = sorted(str(a))

print ("Multiplication:", f)
print("Reverse:",h,y,v,z)
print("Sorted 4-digit number",x)