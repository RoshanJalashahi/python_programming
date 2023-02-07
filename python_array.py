cars = ["toyota","BMW","volvo"]
cars[0] = "mercedes"
print(cars)
print(len(cars))
for x in cars:
    print(x)

#You can use the append() method to add an element to an array.

cars = ["toyota","BMW","volvo"]
cars.append("honda")
print(cars)
print(cars.pop(1))
print(cars.remove("volvo"))
