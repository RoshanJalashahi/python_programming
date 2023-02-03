thisdicton = {
    "name" : "Parbati",
    "home" : "Dhading",
    "status" : "Love",
    "Year" : "2023 - 10 -20"
}

print(thisdicton)

thisdicton = {
    "name" : "Parbati",
    "home" : "Dhading",
    "status" : "Love",
    "Year" : "2023 - 10 -20"
}
print(thisdicton["name"])

#duplicate values will override
thisdicton = {
    "name" : "Parbati",
    "home" : "Dhading",
    "status" : "hate",
    "status" : "Love",
    "Year" : "2023 - 10 -20"
}
print(thisdicton)
print(len(thisdicton))
print(type(thisdicton))

#constructor dictionary
thisdicton = dict(name = "Parbati",home = "dhading", status = "love", year = "2023-10-20")
print(thisdicton)