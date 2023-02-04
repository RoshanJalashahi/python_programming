thisdicton = {
    "name" : "Parbati",
    "home" : "Dhading",
    "status" : "hate",
    "Year" : "2023 - 10 -21"
}
thisdicton.pop("status")
print(thisdicton)


#popitem() method removes random items
thisdicton = {
    "name" : "Parbati",
    "home" : "Dhading",
    "status" : "love",
    "Year" : "2023 - 10 -21"
}
thisdicton.popitem()
print(thisdicton)

#del can remove  both specific and delete whole dict

thisdicton = {
    "name" : "Parbati",
    "home" : "Dhading",
    "status" : "love",
    "Year" : "2023 - 10 -21"
}
del thisdicton["status"]
print(thisdicton)
#del thisdicton
#print(thisdicton)

thisdicton = {
    "name" : "Parbati",
    "home" : "Dhading",
    "status" : "love",
    "Year" : "2023 - 10 -21"
}
thisdicton.clear()
print(thisdicton)