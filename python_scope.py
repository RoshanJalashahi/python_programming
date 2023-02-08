#A variable is only available from inside the region it is created. This is called scope.
#A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
def myfunc():
     x = 300
     print(x)
myfunc()


#function inside function
def myfun():
    x = 300
    def myinnerfun():
        print(x)
    myinnerfun()
myfun()

#global variable
x = 35
def myfunc():
    print(x)
myfun()
print(x)

x = 30

def myfunc():
  print(x)

myfunc()

print(x)





x = 200
def my():
    x = 100
    print(x)
my()

print(x)

#global keyword
def myfu():
    global x
    x = 150
    print(x)
myfu()

print(x)


x = 300
def myy():
    global x
    x = 98
myy()

print(x)
