x = lambda  a : a + 10
print(x(5))

x = lambda a,b : a*b
print(x(5,2))

def myfunc(n):
    return lambda a : a * n
mydouble = myfunc(2)
print(mydouble(11))


def myfunct(n):
    return lambda a : a * n
mydouble = myfunc(2)
mytriple = myfunc(3)
print(mydouble(11))
print(mytriple(11))