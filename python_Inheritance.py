class person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def printname(self):
        print(self.fname,self.lname)

p1 = person("Prabina","khatri")
p1.printname()

class person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname,self.lname)

class child(person):
    pass

x = person("prabina","khatri")
x.printname()

class person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def printname(self):
        print(self.fname,self.lname)

class child(person):
    def __init__(self, fname , lname):
        person.__init__(self, fname, lname)
x = person("prabinna","khatrii")
x.printname()


class person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def printname(self):
        print(self.fname,self.lname)

class child(person):
    def __init__(self, fname , lname):
        super().__init__(self, fname, lname)
x = person("prabinnaa","khatrii")
x.printname()

class student:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

class child(student):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2024

x = child("PRABINA","Khatri")
print(x.graduationyear)

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.graduationyear)

'''
class person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname,self.lname)

class student(person):
    def __init__(self, fname, lname, year):
        super().__init__(fname,lname)
        self.graduationyear = 2024

    def welcome(self):
        print("welcome", + self.fname, +self.lname, "to the class of", self.graduationyear)

x = student("prabina","khatri", 2024)
x.welcome()'''

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("prabina", "khatri", 2019)
x.welcome()
