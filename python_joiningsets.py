sets = {"Parbati","prapti","prabina"}
set2 = {"roshan","love"}
set3 = set2.union(sets)
print(set3)

#The intersection_update() method will keep only the items that are present in both sets.
sets = {"parbati","prapti","prabina"}
set2 = {"roshan","love","parbati"}
set2.intersection_update(sets)
print(set2)

sets = {"parbati","prapti","prabina"}
set2 = {"roshan","love","parbati"}
set3 = set2.intersection(sets)
print(set3)

#The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
sets = {"parbati","prapti","prabina","hate"}
set2 = {"roshan","love","hate"}
set2.symmetric_difference_update(sets)
print(set2)

sets = {"parbati","prapti","prabina","hate"}
set2 = {"roshan","love","hate"}
set3 = set2.symmetric_difference(sets)
print(set3)