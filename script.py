# Step 1: Create an empty list called my_list
my_list = []

# Step 2: Append elements 10, 20, 30, 40 to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
# At this point, my_list is [10, 20, 30, 40]

# Step 3: Insert the value 15 at the second position (index 1)
my_list.insert(1, 15)
# Now, my_list becomes [10, 15, 20, 30, 40]

# Step 4: Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])
# After extending, my_list is [10, 15, 20, 30, 40, 50, 60, 70]

# Step 5: Remove the last element from my_list using pop()
my_list.pop()  # Removes the last element (70)
# Now, my_list is [10, 15, 20, 30, 40, 50, 60]

# Step 6: Sort my_list in ascending order
my_list.sort()
# my_list becomes [10, 15, 20, 30, 40, 50, 60] (already sorted in this case)

# Step 7: Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print("The index of 30 in my_list is:", index_of_30)

# Optional: Print the final list to see the complete result
print("Final list:", my_list)
