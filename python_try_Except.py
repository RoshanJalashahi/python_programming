'''The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.'''

try:
    print(x)
except:
    print("An execption error occured")


try:
    print(x)
except NameError:
    print("variable x is not defined")
except:
    print("something esle went wrong")


try:
    print(x)
except:
    print("something went wrong")
finally:
    print("the 'try' exception is finished")


try:
    f = open("demofile.txt")
    try:
        f.write("Hi prabina i love you")
    except:
        print("something went wrong")
    finally:
        f.close()
except:
    print("something went wrong when opening the file")


x = -1

if x < 0:
    raise Exception("sorry, no numbers below zero")

x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed")