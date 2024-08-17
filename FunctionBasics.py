#functions -> block of code which can be reused

def trialfunction():
    print("Hello, World")
trialfunction()

def trialfn(x):
    print(x+"World")
trialfn("Yellow")

def doubleparameter(x,y):
    print(x+" "+y)
doubleparameter("sweet","world")

numbers=[1,2,3,4,5,6,7,8]
for x in numbers:
    print(x)

x="Fruits"
for a in x:
    print(a)

for x in numbers:
    print(x)
    if x==5:
        break

for y in numbers:
    if y==4:
        continue
    print(y)

#Looping statements
#for loop
for x in range (40, 100):
    print(x)

#while loop
i=0
while i<6:
    print(i)
    i=i+1

i=1
while i<6:
    i+=1
    print(i)
    if i==3:
        break

i=1
while i<6:
    i+=1
    print(i)
    if i==3:
        continue

def trial (x,y):
    print(x+" "+y)
trial("hello", "world")

list=['car', 'bus', 'bike', 'scoot']
def loop(x):
    print(x*3)
loop(list)

def map_simple(crazy,list):
    for items in list:
        crazy(items)
map_simple(loop,list)


