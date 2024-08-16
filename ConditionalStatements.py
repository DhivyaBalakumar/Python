#method 1
a=30; b=300;
if a>b:
    print("a is greater than b")
elif(a<b):
    print("a is lesser than b")
else:
    print("a is equal to b")

#method 2
if a>b: print("a is greater than b")
else: print("otherwise")

#method 3
x=20; y=200;
print("x is lesser than y") if x<y else print("x is greater than y")

#and or conditions
c=100
print(a,b,c)

#and condition
if a>c and c>b:
    print("a")
elif a>b and b>c:
    print("c")
else:
    print("None!")

#or condition
if a>b or c>a:
    print(a)
else:
    print("none")


