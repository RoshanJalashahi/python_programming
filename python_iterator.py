#Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
tuplee = ("Prabina","prapti","prabati")
myit = iter(tuplee)

print(next(myit))
print(next(myit))
print(next(myit))

tuplee = "Parbati"
myy = iter(tuplee)

print(next(myy))
print(next(myy))
print(next(myy))
print(next(myy))
print(next(myy))
print(next(myy))
print(next(myy))

tupp = ("Parbati","prapti","prabina")
for x in tupp:
    print(x)

class mynumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = mynumber()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))



