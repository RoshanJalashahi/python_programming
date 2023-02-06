name = [ "parbati","prabina","prapti"]
for x in name:
    print(x)

for x in "parbati":
    print(x)


#with a break statement we can break the for loop
name = ["parbati","prabina","prapti"]
for x in name:
    print(x)
    if x == "prabina":
        break


name = ["parbati","prabina","prapti"]
for x in name:
    if x == "prabina":
        print(x)



name = ["parbati","prabina","prapti"]
for x in name:
    if x == "prapti":
        continue
        print(x)


#range() function

for x in range(6):
    print(x)

for x in range(2,6):
    print(x)

for x in range(2,33,6):
    print(x)

#esle if
for x in range(6):
    print(x)
else:
    print("it is over")


name = ["parbati","prabina","prapti"]
status = ["Heart","love","cutie"]
for x in name:
    for y in status:
       print(x,y)


for x in[1,0,2]:
    pass