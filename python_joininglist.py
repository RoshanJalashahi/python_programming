list1 = ["banana", "Orange", "Kiwi", "cherry"]
list2 =[1 ,2 ,3 ,98,100]
list3 = list1+list2
print(list3)

list1 = ["banana", "Orange", "Kiwi", "cherry"]
list2 =[1 ,2 ,3 ,98,100]
for x in list1:
    list2.append(x)
print(list2)

list1 = ["banana", "Orange", "Kiwi", "cherry"]
list2 =[1 ,2 ,3 ,98,100]
list1.extend(list2)
print(list1)