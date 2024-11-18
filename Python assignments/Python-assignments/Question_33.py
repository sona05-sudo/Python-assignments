"""Write a program which accepts a sequence of comma‐separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')"""

def generate_list_and_tuple():
    # Accept input from the user
    user_input = input("Enter a sequence of comma-separated numbers: ")
    
    # Generate a list from the input
    number_list = user_input.split(",")
    
    # Generate a tuple from the list
    number_tuple = tuple(number_list)
    
    # Print the results
    print("List:", number_list)
    print("Tuple:", number_tuple)

# Call the function to execute the program
generate_list_and_tuple()
