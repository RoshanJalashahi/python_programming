class myclass:
    x = 5
p1 = myclass()
print(p1.x)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("parbati", 36)

print(p1.name)
print(p1.age)


class per:
    def __init__(self, name ,age):
        self.name = name
        self.age = age
p1 = per("prabina", 18)

print(p1.name)
print(p1.age)
print(p1)

class perr:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"

p1 = perr("prabati",32)
print(p1)

class yoyo:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello i love you " + self.name)

p1 = yoyo("Prabati",33)
p1.myfunc()


class love:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
    def myy(abc):
        print(" hello i love you " + abc.name)

p1 = love("prabina",18)
p1.myy()

