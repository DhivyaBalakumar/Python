#Correct method of naming variables
_a="apple"
a="apple"
a2="apple"
print(a)

"""
Wrong method of naming variables
@a
#a
%a    #no spl char apart from _ is allowed
2a    #cannot start with a number
"""

x=5
x=("john")
print(x)

j=str(5)
print(j, type(j))

k=int(5)
print(k, type(k))

l=float(5)
print(l, type(l))

#a print statement can have more than one parameter at once

#methods of assigning values to variables
#method1
#individual
c="cat"
d="dog"
e="ele"

#method2
#cumulative
f,g,h= "a", "b", "c"

# f, g, h = "a", "b"  ValueError: not enough values to unpack (expected 3, got 2)
# print(f, g, h)

#method3
#multiple variables to one value
m=n=o= "oranges"
print(m,n,o)