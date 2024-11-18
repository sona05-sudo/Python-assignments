#Write a Python program to find the average of n numbers using list
def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def input_numbers():
    user_input = input("Enter numbers separated by spaces: ")
    # Convert input string into a list of floats
    input_list = [float(num) for num in user_input.split()]
    return input_list

# Get the list of numbers from the user
numbers = input_numbers()

# Calculate and print the average
average = calculate_average(numbers)
print("The average of the entered numbers is:", average)
