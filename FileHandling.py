f=open("TextFile","r")
print(f.readline())
print(f.read(100))
print(f.readlines(2))

f=open("TextFile", "w")
print(f.write("Welcome"))
print(f.write("hope you have fun learning file handling in python"))

"""
@overload def open(file: int | str | bytes | PathLike[str] | PathLike[bytes],
         mode: Literal["r+", "+r", "rt+", "r+t", "+rt", "tr+", "t+r", "+tr", "w+", "+w", "wt+", "w+t", "+wt", "tw+", "t+w", "+tw", "a+", "+a", "at+", "a+t", "+at", "ta+", "t+a", "+ta", "x+", "+x", "xt+", "x+t", "+xt", "tx+", "t+x", "+tx", "w", "wt", "tw", "a", "at", "ta", "x", "xt", "tx", "r", "rt", "tr", "U", "rU", "Ur", "rtU", "rUt", "Urt", "trU", "tUr", "Utr"] = "r",
         buffering: int = -1,
         encoding: str | None = None,
         errors: str | None = None,
         newline: str | None = None,
         closefd: bool = True,
         opener: (str, int) -> int | None = None) -> TextIOWrapper
"""

#using loop
f=open("TextFile")
for x in f:
    print(x)

f.close()

#writing to a file -> open in append mode
f=open("TextFile", "a")
f.write("a new line now")
f.close()

f=open("TextFile", "r")
print(f.read())

#Write mode
#the whole file content will be rewritten with this one sentence
f=open("TextFile", "w")
f.write("this was the file content prior to writing: Welcomehope you have fun learning file handling in pythona new line now"
        "this is the file content after writing, the content has been rewritten")
f.close()

f=open("TextFile","r")
print(f.read())

#create a new file (X->create)
f=open("TextFile","x")

#even the write mode creates a file if it isn't already existing
f=open("TextFile","w")

#deleting/removing a file
import os
os.remove("TextFile")
if os.path.exists("TextFile"):
    os.remove("TextFile")
else:
    print("file does not exist")
