# sorting in python
fruits = ["apple", "grapes", "cherry", "kiwi", "mango"]
fruits.sort()
print(fruits)

#for numbers
numbers = [20,50,5,1,60,40]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

#sorting according to near of 50
def myfunc(n):
    return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#insensitive function
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)
thislist.reverse()
print(thislist)