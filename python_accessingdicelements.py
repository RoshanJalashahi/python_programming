thisdicton = {
    "name" : "Parbati",
    "home" : "Dhading",
    "status" : "hate",
    "status" : "Love",
    "Year" : "2023 - 10 -20"
}
x = thisdicton["name"]
print(x)
x = thisdicton.get("name")
print(x)
x = thisdicton.keys()
print(x)

thisdicton = {
    "name" : "Parbati",
    "home" : "Dhading",
    "status" : "Love",
    "Year" : "2023 - 10 -20"
}
x = thisdicton.keys()
print(x)
thisdicton["time"] = "forever"
print(thisdicton)
print(x)

#values()
thisdicton = {
    "name" : "Parbati",
    "home" : "Dhading",
    "status" : "Love",
    "Year" : "2023 - 10 -20"
}
x = thisdicton.values()
print(x)
thisdicton["time"] = "forever"
print(x)


thisdicton = {
    "name" : "Parbati",
    "home" : "Dhading",
    "status" : "Love",
    "Year" : "2023 - 10 -20"
}
x = thisdicton.items()
print(x)
thisdicton["time"] = "forever"
print(x)


thisdicton = {
    "name" : "Parbati",
    "home" : "Dhading",
    "status" : "Love",
    "Year" : "2023 - 10 -20"
}
if "name" in thisdicton:
    print("yes","i love her")
