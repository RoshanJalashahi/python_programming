# in pyhton we can add list

#By append() method we can add at last of string
mylist = ["Prabina ","Loves"]
mylist.append("Roshan")
print(mylist)

#By insert() method we can add list to any index
mylist = ["Prabina","Loves","Forever"]
mylist.insert(2,"Roshan")
print(mylist)

#Merging two lsit by .extend
mylove = ["Prabina","loves"]
me = ["forever","Roshan"]
mylove.extend(me)
print(mylove)