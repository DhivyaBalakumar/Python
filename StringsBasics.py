x="Hello, World"
print(x[0])
print(x[1])
print(x[10])
print(x[11])
# print(x[12])     #IndexError

#looping through strings
for a in x:
    print(a)

#length of the string
print(len(x))

print("World" in x)
print("world" in x)
print("like" in x)

print(x[2:5])
print(x[:5])
print(x[2:])

#negative indexing
print(x[-5:-2])

#modifying strings
print(x.upper())
print(x.lower())

#removing spaces
print(x.strip())
print(x.lstrip())
print(x.rstrip())

print(x.replace("H","Y"))
print(x.split(","))

a="Hello"
b="World"
print(a+b)
print(a+" "+b)