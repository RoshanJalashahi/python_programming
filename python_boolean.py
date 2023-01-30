# boolean is used to evaluated expressions in python
a = "Prabina"
b ="Roshan"
c = 10>11
print(bool(a))
print(bool(b))
print(bool(c))

a = 100
b = 25
if a < b:
    print("a is larger")
else:
    print("b is smaller")

''' any string is true except empty one, any number is true except o , any list tuples are true except null'''
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
