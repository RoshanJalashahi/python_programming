import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())


'''
The split() Function
The split() function returns a list where the string has been split at each match:'''

import re
txt = "i wish we had never met"
x = re.split("\s",txt)
print(x)
y = re.split("\s",txt,1)
print(y)


'''
The sub() Function
The sub() function replaces the matches with the text of your choice:'''
import re
txt = "hey vagwan sadhai ma sanga yesto kina hunxa"
x = re.sub("\s","   ",txt)
print(x)
y = re.sub("\s"," ? ",txt,2)
print(y)


'''
Match Object
A Match Object is an object containing information about the search and the result.'''
import re
txt = "sabai tw garesakyo tmle, k xa rw baki aba tmro rw mera bichma, tmlai j maan lagxa tei gara"
x = re.search("tm",txt)
print(x)


import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

import re
txt = "jau Samaya aba tmi aafno bato , ma ni aafno bato"
x = re.search(r"\bS\w+", txt)
print(x.string)

import re
txt = "i wish we had Never meet , jau aba kei relationship nai xaina aba"
x = re.search(r"\bN\w+", txt)
print(x.group())