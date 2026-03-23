# Create sets
set1 = {15, 4, 3, 64, 50}
set2 = {64, 50, 46, 7, 18}

# Access set elements (iterate through set)
print("Set 1 elements:")
for element in set1:
 print(element, end=" ")


for element in set2:
 print(element, end=" ")
 print()

# Union of sets
union_set = set1.union(set2)
print("Union of Set1 and Set2:", union_set)

# Intersection of sets
intersection_set = set1.intersection(set2)
print("Intersection of Set1 and Set2:",
intersection_set)

# Difference of sets (Set1 - Set2)
difference_set = set1.difference(set2)
print("Difference (Set1 - Set2):", difference_set)

# Difference of sets (Set2 - Set1)
difference_set2 = set2.difference(set1)
print("Difference (Set2 - Set1):", difference_set2)