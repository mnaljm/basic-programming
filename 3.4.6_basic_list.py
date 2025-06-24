hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
middleReplacement = int(input("Enter a new middle number: "))
hat_list[2] = middleReplacement  # Replace the middle number (index 2) with user input.
# Step 2: write a line of code that removes the last element from the list.
hat_list.pop()  # Remove the last element from the list.
# Step 3: write a line of code that prints the length of the existing list.
print("Length of the hat list:", len(hat_list))  # Print the length of the list.
print(hat_list)
