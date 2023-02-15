import re

txt = "the rain in spain"
x = re.search("^the.*spain$", txt)
if x:
    print("yes its over")
else:
    print("i will never repeat")

x = re.findall("ai",txt)
print(x)


import re
txt = "oh god why always me"
x = re.findall("prabina",txt)
print(x)

if x:
    print("i wish i had stone heart")
else:
    print("i wish we had never met")