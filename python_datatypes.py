''' Pyhton has following built in data types as below:-'''
''' 
Text  types =  string 
numeric types  =  int , float , complex
sequence types =  list[], tuple(), range(6)
mapping type = Dict
set types =  set, frozenset
boolean types =  bool
binary types =  bytes ,  bytearray ,  memoryview
non types =  Nontypes
'''

x =  'Prabina '
print(x)

x =  10
print(x)
x = 20.0
print(x)
x = 1j
print(x)

x = list(("Roshan ","Prabina","Prapti"))
print(x)
x = ("Roshan","Prabina","Prapti")
print(x)
x = range(6) # range
print(x)

#mapping
x = {"name":"Prabina","age":18}
print(x)
x = dict(name="Prabina",age=18)
print(x)

 #set
x = {"apple","banana","orange"}
print(x)

# frzen set
x = frozenset({"apple","banana","grapes"})
print(x)

# boolean
x = True
print(x)

# BINARY
x =b"hello"
print(x)
x = bytearray(6)
print(x)
x = memoryview(bytes(5))
print(x)
x = None
print(x)