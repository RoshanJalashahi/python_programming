'''
String format()
The format() method allows you to format selected parts of a string.

Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?

To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method:
'''

price = 49
txt = "The  price is {} dollars"
print(txt.format(price))

you = "The price is {:.2f} dollars"
print(txt.format(you))

price = 400
quantity = 5
itemno = 553
myorder = "i want {} markers of item number{} for {:.2f} dollars."
print(myorder.format(quantity,itemno,price))

name = "Prabina"
age = 18
love = "Her name is {0}. {0} is {1} years old"
print(love.format(name,age))

