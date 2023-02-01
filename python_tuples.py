#tuples can contain duplicate datas
thistuple = ("Prabina","loves","Roshan","Forever","loves")
print(thistuple)
thistuple = ("Prabina","loves","Roshan","Forever","loves",1,20.0,True)
print(thistuple)
print(type(thistuple))


thistuple = tuple(("Prabina","loves","Roshan","Forever","loves",1,20.0,True))
print(thistuple)

#for single item tuple we use comma
thistuple = ("prabina",)
print(thistuple)
print(type(thistuple))