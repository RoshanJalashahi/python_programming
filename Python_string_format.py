# as we know that we cannot add string and integer using + operator so, we use format () method
age = 18
txt = '''My name is Prabina, i am {} years old'''
print(txt.format(age))

age = 18
study = 12
stu = 49
txt = " my name is Prabina, i am {2} years old, i study in {0} class, there are total {1} in my class"
print(txt.format(study,stu,age))