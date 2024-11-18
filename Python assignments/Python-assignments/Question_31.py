#Write a Python program to perform Linear search.
def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

def input_numbers():
    user_input = input("Enter numbers separated by spaces: ")
    # Convert input string into a list of integers
    input_list = [int(num) for num in user_input.split()]
    return input_list

# Get the list of numbers from the user
numbers = input_numbers()

# Input the target number to search for
target = int(input("Enter the number to search for: "))

# Perform linear search
result = linear_search(numbers, target)

# Print the result
if result != -1:
    print(f"The number {target} is found at index {result}.")
else:
    print(f"The number {target} is not found in the list.")
