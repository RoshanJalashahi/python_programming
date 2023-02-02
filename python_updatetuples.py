x = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
y = list(x)
y[1] = "Prabina"
x =tuple(y)
print(x)

# through use of append()
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
y = list(thistuple)
y.append("Prabina")
thistuple = tuple(y)
print(thistuple)

# creating a tuple and adding tuples
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
y = ("Prabina",)
thistuple = thistuple+y
print(thistuple)

# removing item from tuples
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

# completly deleting tuples
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
del tuple
print(thistuple) # this will produce error because tuple is no lONGER