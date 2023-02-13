import json
x = {
    "name": "Parabati Acharya",
    "age": "35",
    "address": "Dhading",
    "married": True,
    "Children": ("Prabina","Prapti"),
    "affair": "with me",
    "cars": [
        {"model": "MERCESDES", "color": "Blue Dark"},
        {"model": "LS200", "color": "Blach Dark"}
    ]
}
y = json.dumps(x)
print(x)
print(json.dumps(x, indent=4, sort_keys=True))
print(json.dumps(x, indent=4, separators=(". ", " = ")))