#there are many methods to remove list elements like remove(), pop(), clear(),del()

mylist = ["Prabina","Loves","Hate","Roshan"]
mylist.remove("Hate")
print(mylist)

mylist = ["Prabina","Loves","Hate","Roshan"]
mylist.pop(2)
print(mylist)

mylist = ["Prabina","Loves","Roshan","never"]
mylist.pop()
print(mylist)

#clear will empty the list
mylist = ["Prabina","Loves","Roshan","never"]
mylist.clear()
print(mylist)

#del will delete entire list
mylist = ["Prabina","Loves","Roshan","never"]
del mylist