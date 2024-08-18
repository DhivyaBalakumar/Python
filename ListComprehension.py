#list comprehension is basically shortening the code intended for string operations

fruits=["apple", "banana", "grape", "mango", "kiwi"]
newfruits=[]
# oldfruit=[]

for x in fruits:
    if "a" in x:
        newfruits.append(x)
print(newfruits)

# for y in fruits:
#     if "o" in fruits:
#         oldfruit.append(y)
# print(oldfruit)

print(fruits)

oldfruits=[x for x in fruits if x!="banana"]
print(oldfruits)

bear=[x for x in fruits]
print(fruits)

cat=[x.upper() for x in fruits]
print(cat)

numbers=[x for x in range (10)]
print(numbers)

numbers1=[x for x in range(100) if x<50]
print(numbers1)

fruits100=["bananas", "apples", "kiwis", "oranges", "apricots"]
madagascar=[x if x!="bananas" else "oranges" for x in fruits100]
print(madagascar)