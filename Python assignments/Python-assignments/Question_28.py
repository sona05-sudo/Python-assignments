#Write a Python program to take a input from user in a list and print it.
def input_list():
    user_input = input("Enter elements of the list separated by spaces: ")
    # Split the input string into a list of elements
    input_list = user_input.split()
    return input_list

# Get the list from the user
user_list = input_list()

# Print the list
print("The list you entered is:", user_list)
