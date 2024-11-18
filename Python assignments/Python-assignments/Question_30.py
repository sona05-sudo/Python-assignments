#Write a Python program to find the largest element in the list.
def find_largest(numbers):
    if not numbers:
        return None  # Return None if the list is empty
    largest = numbers[0]  # Assume the first number is the largest
    for num in numbers:
        if num > largest:
            largest = num  # Update largest if a bigger number is found
    return largest

def input_numbers():
    user_input = input("Enter numbers separated by spaces: ")
    # Convert input string into a list of floats
    input_list = [float(num) for num in user_input.split()]
    return input_list

# Get the list of numbers from the user
numbers = input_numbers()

# Find and print the largest element
largest_element = find_largest(numbers)
if largest_element is not None:
    print("The largest element in the list is:", largest_element)
else:
    print("The list is empty.")
