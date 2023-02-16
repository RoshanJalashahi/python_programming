'''
To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content


'''

#f = open("Prabina2.txt", "a")
#f.write("tmi sadhai khusi rahirahanu, yehi ho mero subhakamana")
#f.close()

#f = open("Prabina2.txt", "r")
#print(f.read())
#f.close()

#f = open("mylov.txt", "w")
import os
if os.path.exists("mylove.txt"):
    os.remove("mylove.txt")
else:
    print("the file does not exit")