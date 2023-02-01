# list loop
mylist = ["Prabina","Roshan","Lovers"]
for x in mylist:
    print(x)

#list  loop through rsnged () and len()
mylist = ["Prabina","Roshan","Lovers"]
for i in range(len(mylist)):
    print(mylist[i])

    #using while loop
mylist = ["Prabina","Roshan","Lovers"]
i = 0
while i<len(mylist):
    print(mylist[i])
    i = i+1

    mylist = ["Prabina", "Roshan", "Lovers"]
    [print(x) for i in mylist]