sets = {"Parbati","prapti","prabina","hate"}
sets.remove("hate")
print(sets)

sets = {"Parbati","prapti","prabina"}
sets.discard("hate")
print(sets)

#pop() will remove any random elements
sets = {"Parbati","prapti","prabina","hate"}
x = sets.pop()
print(x)
print(sets)

#clear () method will empty sets
sets = {"Parbati","prapti","prabina"}
sets.clear()
print(sets)

#del() will completely delete the set

sets = {"Parbati","prapti","prabina"}
del sets
print(sets)