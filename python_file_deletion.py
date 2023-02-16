import os
if os.path.exists("mylov.txt"):
    os.remove("mylov.txt")
else:
    print("the file does not exit")