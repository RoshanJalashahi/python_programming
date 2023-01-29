'''Python has mainly three types of numbers
1) int type
2) float type
3) complex types'''

x = 1
y = 2.01
z = 3+9j
print(type(x))
print(type(y))
print(type(z))

# integer types
''' integer numbers can be any whole , negative, positive but without decimal numbers'''
x = 1111111
y = 2
z = -12345
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))

# float numbers
''' a float numbers may be any whole numbers, positive numbers, negative numbers must contain a atleast one or more decimal'''
x = 1.0
y = 2.000035
z = -3.45
 # notes a float numbers can be scitific numbers representation i.e we can use exponential i.e E, e
x = 2e3
y = 12E4
Z = -12.E89
print(type(x))
print(type(y))
print(type(z))

# complex numbers are represented by an j
x =  3+2j
y = -2j
z =  5j
print(type(x))
print(type(y))
print(type(z))

''' type casting '''
x = 1
y = 2.56
z = 5j
# int to float
a = float(x)
print(a)
 # float to int
b = int(y)
print(b)

#int to complex
c = complex(x)
print(c)