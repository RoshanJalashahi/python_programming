a = 12
b = 22
if a>b:
    print("a is greater than b")
else:
    print("a is less than b")

a = 22
b = 22
if a>b:
    print("a is greater than b")
elif a == b:
    print("both are equals")


a = 2200
b = 22
if b > a:
    print("b is greater than a")
elif a == b:
    print("both are equals")
else:
    print("a is greater")


a = 2200
b = 22
if a > b: print("a is greater")

a = 2200
b = 22000
print("a is greater") if a>b else print("b is greater")

a = 700
b = 500
c = 200
if a>b and b > c:
    print("both are greater")


a = 700
b = 500
c = 200
if a>b or c > b:
    print("atleaast one of them is greater")


x = 40
if x > 10:
    print(" x is greater")
    if x > 20:
        print("x is greater tham 20")
    else:
        print("x but not above 20")