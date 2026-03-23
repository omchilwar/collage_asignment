# Create a list
numbers = [100, 65, 9, 6, 515]

# Access list elements
print("Original List:", numbers)
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Add elements
numbers.append(20)
numbers.insert(2, 5)
print("List after adding elements:",
numbers)

# Remove elements
numbers.remove(515)
numbers.pop()
print("List after removing elements:",
numbers)

# Sort list elements
numbers.sort(reverse=True)
print("Sorted List:", numbers)

# Reverse list elements
numbers.reverse()
print("Reversed List:", numbers)