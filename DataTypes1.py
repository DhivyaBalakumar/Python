"""
There are three numeric data types in python
1) int -> whole numbers; +ve or -ve
2) float -> decimal point numbers
3) complex -> j is the imaginary part
"""
x=1
print(x)
print(type(x))

y=1.00000
print(y)
print(type(y))

z=1j
print(z)
print(type(z))

#datatype interconversions

# 1)int to float

print(x)
print(type(x))
a=float(x)
print(a)
print(type(a))

# 2) float to int

print(y)
print(type(y))
b=int(y)
print(b)
print(type(b))

# 3) int to complex

print(x)
print(type(x))
c=complex(x)
print(c)
print(type(c))