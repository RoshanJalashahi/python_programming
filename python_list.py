# Python has four built in data types to store collection of data i.e List , Tuples, Set, Dictionary
 # list in Python
mylist = ["Prabina","Roshan","Prapti"]
print(mylist)

# list allows to print duplicate values
mylist = ["Prabina","Roshan","Prapti","Sudip","Prabina"]
print(mylist)
print(len(mylist))

#list with multiple data types
mylist = ["Prabina",18,"Prapti",12,40000.00]
print(mylist)

#findout datatypes of list
mylist = ["Prabina","Loves","Roshan"]
print(type(mylist))

#list construstor using list() function
mylist = list(("Roshan","Likes","Prabina"))
print(mylist)