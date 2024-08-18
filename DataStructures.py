#Data structure
#List
"""
Lists are ordered
changeable/mutable
allow duplicates
"""
list=["string",10,10.0,True,"Bool"]
print(list)

#Accessing the elements
print(list[0])
print(list[4])
print(list[2:5])
print(list[2:])
print(list[:5])

#changing list elements
list[2]="scoot"
print(list)

list[1:3]=("scoot", "scoot2")
print(list)

list.insert(3,"Jeep")
print(list)

list.append("Vehicle")
print(list)


#Tuple
"""
Tuples are ordered
immutable/cant be changed
allow duplicates
"""

#tuple->string
tuple=("HiThisIsAStringButATuple")
print(tuple,type(tuple))

tup="tuple?"
print(tup, type(tup))

tupp=("tup1", "tup2" , "tup3")
print(tupp, type(tupp))

tuplee=("string", 10, 10.0, True, "Bool", "string")
print(tuplee, type(tuplee))

tupleee=("car",); tuplle=("car")
print(tupleee, type(tupleee), tuplle, type(tuplle))

#accessing values of tuples
print(tuple[2])
print(tuple[0])

#using index values
print(tuple[2:5])
print(tuple[2:])
print(tuple[:5])
print(tuple[0:])
print(tuple[:])

#tuple.append("oranges")  ->AttributeError
# z=("orange", "apple", "pinepple", "kiwi")
#How to add elements/ alter a tuple
# y= list(z)
# y[1]=("bananas")
# x=tuple(y)
# print(x, type(x))

# my_tuple = (1, 2, 3)
# my_list = list(my_tuple)
# print(my_list)  # Output: [1, 2, 3]

#Dictionary
"""
dictionaries are unordered
mutable/changeable
do not allow duplicate values
"""

dictt={
    "name":"Raj",
    "age":26,
    "vehicle":"ford",
    "DOB":"12-12-12"
}
print(dictt)

#duplicate keys lead to overriding of values
print(len(dictt))
print(type(dictt))

duf={
     "name":"Raj",
     "age":26,
     "vehicle":"ford",
     "DOB":"12-12-12"
 }
print(duf)
x=duf["vehicle"]  #->SQUARE BRACKETS
print(x)
y=duf.get("vehicle")
print(y)

duf["vehicle"]="bike"
print(duf)
#update method
duf.update({"name":"XYZ"})
duf["color"]="pink"     #adding a key value pair

#removing a key value pair
duf.pop(("vehicle"))




